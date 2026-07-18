import React, { useEffect, useState, useRef } from 'react';
import { Share2, Search, ZoomIn, ZoomOut, Maximize } from 'lucide-react';

interface CytoscapeNode {
  data: {
    id: string;
    label: string;
    type: string;
    name?: string;
    country?: string;
    [key: string]: any;
  };
  classes?: string;
}

interface CytoscapeEdge {
  data: {
    source: string;
    target: string;
    label?: string;
  };
}

interface NetworkData {
  elements: {
    nodes: CytoscapeNode[];
    edges: CytoscapeEdge[];
  };
}

const calculateLayout = (nodes: CytoscapeNode[], edges: CytoscapeEdge[], width: number, height: number) => {
  const getLayer = (type: string) => {
    const t = type.toLowerCase();
    if (t.includes('mine') || t.includes('supplier')) return 0;
    if (t.includes('processing') || t.includes('refiner') || t.includes('refinery')) return 1;
    if (t.includes('material') || t.includes('component')) return 2;
    if (t.includes('battery') || t.includes('cell') || t.includes('plant')) return 3;
    if (t.includes('vehicle') || t.includes('fleet')) return 4;
    return 2;
  };

  const layers: CytoscapeNode[][] = [[], [], [], [], []];
  nodes.forEach(n => layers[getLayer(n.data.type || '')].push(n));

  const nodePositions: Record<string, { x: number, y: number }> = {};
  
  const activeLayers = layers.filter(l => l.length > 0);
  const layerWidth = width / (activeLayers.length + 1);

  let activeLayerIdx = 0;
  layers.forEach((layerNodes) => {
    if (layerNodes.length === 0) return;
    const x = layerWidth * (activeLayerIdx + 1);
    const nodeSpacing = height / (layerNodes.length + 1);
    
    layerNodes.forEach((node, idx) => {
      nodePositions[node.data.id] = {
        x,
        y: nodeSpacing * (idx + 1)
      };
    });
    activeLayerIdx++;
  });

  return nodePositions;
};

const getNodeColor = (type: string) => {
  const t = type.toLowerCase();
  if (t.includes('mine')) return 'text-blue-400 border-blue-500/30 bg-blue-500/10';
  if (t.includes('supplier')) return 'text-sky-400 border-sky-500/30 bg-sky-500/10';
  if (t.includes('processing') || t.includes('refiner') || t.includes('refinery')) return 'text-purple-400 border-purple-500/30 bg-purple-500/10';
  if (t.includes('battery') || t.includes('cell') || t.includes('plant')) return 'text-amber-400 border-amber-500/30 bg-amber-500/10';
  if (t.includes('vehicle') || t.includes('fleet')) return 'text-emerald-400 border-emerald-500/30 bg-emerald-500/10';
  return 'text-slate-400 border-slate-500/30 bg-slate-500/10';
};

export default function NetworkGraph() {
  const [data, setData] = useState<NetworkData | null>(null);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState('');
  
  // Interactivity state
  const [scale, setScale] = useState(1);
  const [position, setPosition] = useState({ x: 0, y: 0 });
  const [isDragging, setIsDragging] = useState(false);
  const dragStart = useRef({ x: 0, y: 0 });

  useEffect(() => {
    const fetchNetwork = async () => {
      try {
        const response = await fetch('/api/v1/supply-chain/dashboard/network');
        if (response.ok) {
          const json = await response.json();
          setData(json);
        }
      } catch (error) {
        console.error('Error fetching network data:', error);
      } finally {
        setLoading(false);
      }
    };
    fetchNetwork();
  }, []);

  if (loading) {
    return <div className="glass p-6 rounded-xl flex flex-col items-center justify-center h-full animate-pulse">Loading Graph Network...</div>;
  }

  const nodes = data?.elements?.nodes || [];
  const edges = data?.elements?.edges || [];

  if (nodes.length === 0) {
    return <div className="glass p-6 rounded-xl text-muted-foreground flex items-center justify-center">No network data available.</div>;
  }

  const filteredNodes = nodes.filter(n => {
    if (!searchTerm) return true;
    const term = searchTerm.toLowerCase();
    return (
      (n.data.type || '').toLowerCase().includes(term) ||
      n.data.id.toLowerCase().includes(term) ||
      (n.data.name && n.data.name.toLowerCase().includes(term)) ||
      (n.data.country && n.data.country.toLowerCase().includes(term))
    );
  });

  const filteredNodeIds = new Set(filteredNodes.map(n => n.data.id));
  const filteredEdges = edges.filter(e => filteredNodeIds.has(e.data.source) && filteredNodeIds.has(e.data.target));

  const width = 1000;
  const height = 600;
  // Use all data for layout calculation so node positions remain stable when filtering
  const nodePositions = calculateLayout(nodes, edges, width, height);

  const handleMouseDown = (e: React.MouseEvent) => {
    setIsDragging(true);
    dragStart.current = { x: e.clientX - position.x, y: e.clientY - position.y };
  };

  const handleMouseMove = (e: React.MouseEvent) => {
    if (isDragging) {
      setPosition({
        x: e.clientX - dragStart.current.x,
        y: e.clientY - dragStart.current.y
      });
    }
  };

  const handleMouseUp = () => setIsDragging(false);

  return (
    <div className="glass p-6 rounded-xl flex flex-col justify-between h-full relative">
      <div className="flex justify-between items-start z-20">
        <div>
          <h2 className="font-semibold text-lg">Multi-Tier Dependency Graph Explorer</h2>
          <p className="text-xs text-muted-foreground mt-1">
            (Nodes: {filteredNodes.length}, Edges: {filteredEdges.length})
          </p>
        </div>
        
        <div className="flex items-center gap-4">
          <div className="relative">
            <Search className="absolute left-2.5 top-2 h-4 w-4 text-muted-foreground" />
            <input 
              type="text" 
              placeholder="Filter by country, name..."
              className="pl-8 pr-4 py-1.5 text-sm bg-background border border-border rounded-lg focus:outline-none focus:ring-1 focus:ring-blue-500"
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
            />
          </div>
          
          <div className="flex gap-1 bg-background border border-border rounded-lg p-1">
            <button onClick={() => setScale(s => Math.min(s + 0.2, 3))} className="p-1 hover:bg-muted rounded"><ZoomIn className="h-4 w-4"/></button>
            <button onClick={() => setScale(s => Math.max(s - 0.2, 0.5))} className="p-1 hover:bg-muted rounded"><ZoomOut className="h-4 w-4"/></button>
            <button onClick={() => { setScale(1); setPosition({x:0, y:0}); }} className="p-1 hover:bg-muted rounded"><Maximize className="h-4 w-4"/></button>
          </div>
        </div>
      </div>

      <div 
        className="my-4 w-full h-[400px] bg-muted/20 border border-border/50 rounded-lg relative overflow-hidden cursor-move"
        onMouseDown={handleMouseDown}
        onMouseMove={handleMouseMove}
        onMouseUp={handleMouseUp}
        onMouseLeave={handleMouseUp}
      >
        <div 
          className="absolute origin-center transition-transform duration-75"
          style={{
            transform: `translate(${position.x}px, ${position.y}px) scale(${scale})`,
            width: '100%',
            height: '100%'
          }}
        >
          <svg viewBox={`0 0 ${width} ${height}`} className="absolute inset-0 h-full w-full pointer-events-none">
            {filteredEdges.map((edge, idx) => {
              const src = nodePositions[edge.data.source];
              const tgt = nodePositions[edge.data.target];
              if (!src || !tgt) return null;
              return (
                <path 
                  key={idx}
                  d={`M ${src.x} ${src.y} L ${tgt.x} ${tgt.y}`} 
                  stroke="rgba(255,255,255,0.2)" 
                  strokeWidth="1.5" 
                />
              );
            })}
          </svg>

          {filteredNodes.map(node => {
            const pos = nodePositions[node.data.id];
            if (!pos) return null;
            return (
              <div 
                key={node.data.id} 
                className={`absolute p-2 rounded-lg text-xs flex flex-col items-center border shadow-sm backdrop-blur-md transition-all ${getNodeColor(node.data.type || '')}`}
                style={{ left: pos.x, top: pos.y, transform: 'translate(-50%, -50%)' }}
                title={JSON.stringify(node.data, null, 2)}
              >
                <span className="font-bold">{node.data.type}</span>
                <span className="text-[10px] opacity-90 max-w-[100px] truncate">
                  {node.data.name || node.data.supplier_id || node.data.id}
                </span>
              </div>
            );
          })}
        </div>
      </div>

      <div className="flex flex-wrap gap-4 text-xs mt-auto">
        <span className="flex items-center gap-1"><span className="h-2 w-2 rounded-full bg-blue-500" /> Mines</span>
        <span className="flex items-center gap-1"><span className="h-2 w-2 rounded-full bg-sky-500" /> Suppliers</span>
        <span className="flex items-center gap-1"><span className="h-2 w-2 rounded-full bg-purple-500" /> Processing/Refiners</span>
        <span className="flex items-center gap-1"><span className="h-2 w-2 rounded-full bg-amber-500" /> Battery/Cells/Plants</span>
        <span className="flex items-center gap-1"><span className="h-2 w-2 rounded-full bg-emerald-500" /> Fleets/Vehicles</span>
      </div>
    </div>
  );
}
