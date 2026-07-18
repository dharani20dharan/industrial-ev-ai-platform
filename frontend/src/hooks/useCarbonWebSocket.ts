import { useState, useEffect, useRef } from 'react';
import { CarbonReport } from '../services/sustainability';

export function useCarbonWebSocket() {
  const [latestReport, setLatestReport] = useState<CarbonReport | null>(null);
  const [connectionStatus, setConnectionStatus] = useState<'connecting' | 'connected' | 'disconnected'>('disconnected');

  const socketRef = useRef<WebSocket | null>(null);
  const reconnectRef = useRef<NodeJS.Timeout | null>(null);

  useEffect(() => {
    let isMounted = true;

    function connect() {
      if (
        socketRef.current &&
        (socketRef.current.readyState === WebSocket.CONNECTING || socketRef.current.readyState === WebSocket.OPEN)
      ) {
        return;
      }

      setConnectionStatus('connecting');
      // Connect to the dashboard stream endpoint defined in backend
      const socket = new WebSocket('ws://localhost:8000/api/v1/ws/dashboard');
      socketRef.current = socket;

      socket.onopen = () => {
        if (!isMounted) {
          socket.close();
          return;
        }
        console.log('📡 Carbon WebSocket connection established.');
        setConnectionStatus('connected');
        
        // Subscribe to carbon updates if the backend requires explicit subscription
        socket.send(JSON.stringify({ action: "subscribe", topic: "ws.carbon.update" }));
      };

      socket.onmessage = (event) => {
        if (!isMounted) return;
        try {
          const data = JSON.parse(event.data);
          
          // Check if this is a carbon update event
          if (data.topic === 'ws.carbon.update' || data.event_type === 'carbon_report_generated') {
            // Depending on how kafka_to_ws_broadcaster sends it, it might be nested under payload
            const payload = data.payload || data;
            setLatestReport(payload as CarbonReport);
          }
        } catch (err) {
          console.warn('Failed to parse websocket message', err);
        }
      };

      socket.onclose = () => {
        if (!isMounted) return;
        console.log('🔴 Carbon WebSocket disconnected.');
        setConnectionStatus('disconnected');
        socketRef.current = null;
        reconnectRef.current = setTimeout(connect, 3000);
      };

      socket.onerror = (err) => {
        console.error('WebSocket encountered error: ', err);
        socket.close();
      };
    }

    connect();

    return () => {
      isMounted = false;
      if (reconnectRef.current) {
        clearTimeout(reconnectRef.current);
      }
      if (socketRef.current) {
        socketRef.current.close();
      }
    };
  }, []);

  return { latestReport, connectionStatus };
}
