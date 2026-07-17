import { useState, useEffect, useRef } from 'react';

export function useFleetData() {
  const [fleet, setFleet] = useState<Record<string, any>>({});
  const [alerts, setAlerts] = useState<any[]>([]);
  const [msgPerSec, setMsgPerSec] = useState(0);

  const socketRef = useRef<WebSocket | null>(null);
  const reconnectRef = useRef<NodeJS.Timeout | null>(null);
  const counterRef = useRef(0);

  useEffect(() => {
    let isMounted = true;

    function connect() {
      // Don't build a new socket if one is already connecting or fully open
      if (
        socketRef.current &&
        (socketRef.current.readyState === WebSocket.CONNECTING || socketRef.current.readyState === WebSocket.OPEN)
      ) {
        return;
      }

      const socket = new WebSocket('ws://localhost:8000/api/v1/telemetry/live');
      socketRef.current = socket;

      socket.onopen = () => {
        if (!isMounted) {
          socket.close();
          return;
        }
        console.log('📡 Telemetry matrix connection established successfully.');
      };

      socket.onmessage = (event) => {
        if (!isMounted) return;
        counterRef.current++;
        try {
          const data = JSON.parse(event.data);
          const vId = data.vehicle_id;
          if (!vId) return;

          // 1. Detect temperature using both payload variants
          const temp = data.motor_temperature_c || data.temperature;

          // 2. Dynamically assign the status flag so the Map and Table UI can read it
          let assetStatus = data.status || "Active";
          if (temp > 40.0) {
            assetStatus = "Critical";
          }

          // 3. Save the modified object with the updated status flag
          const updatedData = { ...data, status: assetStatus };
          setFleet((prev) => ({ ...prev, [vId]: updatedData }));

          // 4. Handle Alert Stack
          if (temp > 40.0) {
            setAlerts((prev) => [
              {
                asset: vId,
                type: 'Critical', // Changed to match your critical check
                msg: `High operational anomaly detected: ${temp.toFixed(1)}°C`,
                timestamp: new Date().toLocaleTimeString()
              },
              ...prev.slice(0, 9)
            ]);
          }
        } catch (e) {
          console.error('Failed to parse frame payload:', e);
        }
      };

      socket.onclose = (event) => {
        // If the component was unmounted, ignore drop notices and drop retry scheduling
        if (!isMounted) return;

        socketRef.current = null;
        console.warn(`Connection dropped (Code: ${event.code}). Retrying downstream handshake...`);

        if (reconnectRef.current) clearTimeout(reconnectRef.current);
        reconnectRef.current = setTimeout(connect, 3000);
      };

      socket.onerror = (error) => {
        // Suppress noisy trace logging if it's just the clean strict-mode teardown drop
        if (!isMounted) return;
        console.error('WebSocket connection error intercepted:', error);
      };
    }

    connect();

    const interval = setInterval(() => {
      if (isMounted) {
        setMsgPerSec(counterRef.current);
        counterRef.current = 0;
      }
    }, 1000);

    return () => {
      isMounted = false;
      clearInterval(interval);
      if (reconnectRef.current) clearTimeout(reconnectRef.current);
      if (socketRef.current) {
        // Clean up the instance cleanly
        const ws = socketRef.current;
        ws.onopen = null;
        ws.onmessage = null;
        ws.onclose = null;
        ws.onerror = null;
        if (ws.readyState === WebSocket.CONNECTING || ws.readyState === WebSocket.OPEN) {
          ws.close();
        }
        socketRef.current = null;
      }
    };
  }, []);

  return { fleet, alerts, msgPerSec };
}
