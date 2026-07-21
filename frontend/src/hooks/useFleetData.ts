import { useState, useEffect, useRef } from 'react';

export function useFleetData() {
  const [fleet, setFleet] = useState<Record<string, any>>({});
  const [alerts, setAlerts] = useState<any[]>([]);
  const [msgPerSec, setMsgPerSec] = useState(0);

  const socketRef = useRef<WebSocket | null>(null);
  const reconnectRef = useRef<NodeJS.Timeout | null>(null);
  const counterRef = useRef(0);

  // Initial REST fetch to seed active vehicles immediately
  useEffect(() => {
    const fetchInitialVehicles = async () => {
      try {
        const res = await fetch("http://localhost:8000/api/v1/simulator/vehicles");
        if (res.ok) {
          const data = await res.json();
          const vehicles = data.vehicles || [];
          const initialMap: Record<string, any> = {};
          vehicles.forEach((v: any) => {
            if (v.vehicle_id) {
              initialMap[v.vehicle_id] = v;
            }
          });
          setFleet((prev) => ({ ...initialMap, ...prev }));
        }
      } catch (err) {
        console.warn("Initial REST vehicle fetch skipped:", err);
      }
    };
    fetchInitialVehicles();
  }, []);

  useEffect(() => {
    let isMounted = true;

    function connect() {
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
        console.log('📡 Live simulator telemetry matrix stream connected.');
      };

      socket.onmessage = (event) => {
        if (!isMounted) return;
        counterRef.current++;
        try {
          const data = JSON.parse(event.data);

          if (data.type === 'HEARTBEAT') return;

          const vId = data.vehicle_id;
          if (!vId) return;

          const temp = data.motor_temperature_c || data.temperature || data.cell_temp || 35.0;
          const statusFlag = data.status || data.driving_state || (data.is_charging ? "CHARGING" : data.is_moving ? "DRIVING" : "IDLE");

          const updatedData = {
            ...data,
            status: statusFlag,
            motor_temperature_c: temp
          };

          setFleet((prev) => ({ ...prev, [vId]: updatedData }));

          // Anomaly/Alert stack
          if (data.active_anomaly || temp > 65.0) {
            setAlerts((prev) => [
              {
                asset: vId,
                type: 'Critical',
                msg: data.active_anomaly ? `Anomaly: ${data.active_anomaly}` : `High temp anomaly: ${temp.toFixed(1)}°C`,
                timestamp: new Date().toLocaleTimeString()
              },
              ...prev.filter(a => a.asset !== vId).slice(0, 9)
            ]);
          }
        } catch (e) {
          console.error('Failed to parse frame payload:', e);
        }
      };

      socket.onclose = (event) => {
        if (!isMounted) return;
        socketRef.current = null;
        if (reconnectRef.current) clearTimeout(reconnectRef.current);
        reconnectRef.current = setTimeout(connect, 3000);
      };

      socket.onerror = (error) => {
        if (!isMounted) return;
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
