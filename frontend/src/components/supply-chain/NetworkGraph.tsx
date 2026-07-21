import React, { useEffect, useState, useRef } from 'react';
import { Search, ZoomIn, ZoomOut, Maximize } from 'lucide-react';

interface CytoscapeNode {
  data: {
    id: string;
    label: string;
    type: string;
    name?: string;
    country?: string;
    supplier_id?: string;
    mine_id?: string;
    material_id?: string;
    plant_id?: string;
    vehicle_id?: string;
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

interface NetworkGraphProps {
  onSelectEntity?: (entityId: string, entityType: string) => void;
  selectedEntityId?: string;
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

const getNodeColor = (type: string, isSelected: boolean) => {
  if (isSelected) return 'text-cyan-200 border-cyan-400 bg-cyan-500/30 ring-4 ring-cyan-400 z-30 scale-110 shadow-cyan-500/50 shadow-lg';
  const t = type.toLowerCase();
  if (t.includes('mine')) return 'text-blue-300 border-blue-500/40 bg-blue-500/15';
  if (t.includes('supplier')) return 'text-sky-300 border-sky-500/40 bg-sky-500/15';
  if (t.includes('processing') || t.includes('refiner') || t.includes('refinery')) return 'text-purple-300 border-purple-500/40 bg-purple-500/15';
  if (t.includes('battery') || t.includes('cell') || t.includes('plant')) return 'text-amber-300 border-amber-500/40 bg-amber-500/15';
  if (t.includes('vehicle') || t.includes('fleet')) return 'text-emerald-300 border-emerald-500/40 bg-emerald-500/15';
  return 'text-slate-300 border-slate-500/40 bg-slate-500/15';
};

export default function NetworkGraph({ onSelectEntity, selectedEntityId }: NetworkGraphProps) {
  const [data, setData] = useState<NetworkData | null>(null);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState('');
  const [hoveredNodeId, setHoveredNodeId] = useState<string | null>(null);

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

  const width = 1400;
  const height = 650;
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
    <div className="glass p-6 rounded-2xl flex flex-col justify-between h-full relative border border-border/80 shadow-2xl w-full">
      <div className="flex justify-between items-start z-20">
        <div>
          <h2 className="font-bold text-xl tracking-tight text-foreground">Interactive Multi-Tier Supply Network</h2>
          <p className="text-xs text-muted-foreground mt-0.5">
            Click nodes to trace dependencies. (Nodes: {filteredNodes.length}, Edges: {filteredEdges.length})
          </p>
        </div>

        <div className="flex items-center gap-3">
          <div className="relative">
            <Search className="absolute left-3 top-2.5 h-4 w-4 text-muted-foreground" />
            <input
              type="text"
              placeholder="Search graph nodes..."
              className="pl-9 pr-4 py-2 text-xs bg-background border border-border rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 font-mono w-48 shadow-inner"
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
            />
          </div>

          <div className="flex gap-1 bg-background border border-border rounded-xl p-1 shadow-sm">
            <button onClick={() => setScale(s => Math.min(s + 0.2, 3))} className="p-1.5 hover:bg-muted rounded-lg transition-colors"><ZoomIn className="h-4 w-4"/></button>
            <button onClick={() => setScale(s => Math.max(s - 0.2, 0.5))} className="p-1.5 hover:bg-muted rounded-lg transition-colors"><ZoomOut className="h-4 w-4"/></button>
            <button onClick={() => { setScale(1); setPosition({x:0, y:0}); }} className="p-1.5 hover:bg-muted rounded-lg transition-colors"><Maximize className="h-4 w-4"/></button>
          </div>
        </div>
      </div>

      <div
        className="my-4 w-full h-[600px] bg-slate-950/90 border border-border/60 rounded-xl relative overflow-hidden cursor-grab active:cursor-grabbing shadow-inner"
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
          {/* SVG Canvas for Curved Bézier Relationship Edges */}
          <svg viewBox={`0 0 ${width} ${height}`} className="absolute inset-0 h-full w-full pointer-events-none">
            {filteredEdges.map((edge, idx) => {
              const src = nodePositions[edge.data.source];
              const tgt = nodePositions[edge.data.target];
              if (!src || !tgt) return null;

              const isConnectedToHover = hoveredNodeId === edge.data.source || hoveredNodeId === edge.data.target;
              const isConnectedToSelected = selectedEntityId === edge.data.source || selectedEntityId === edge.data.target;

              // Smooth cubic Bézier curve formula for gorgeous routing
              const dx = Math.abs(tgt.x - src.x) * 0.5;
              const pathD = `M ${src.x} ${src.y} C ${src.x + dx} ${src.y}, ${tgt.x - dx} ${tgt.y}, ${tgt.x} ${tgt.y}`;

              return (
                <path
                  key={idx}
                  d={pathD}
                  fill="none"
                  stroke={isConnectedToHover || isConnectedToSelected ? "#38bdf8" : "rgba(255,255,255,0.18)"}
                  strokeWidth={isConnectedToHover || isConnectedToSelected ? "2.5" : "1.2"}
                  className="transition-all duration-200"
                />
              );
            })}
          </svg>

          {filteredNodes.map(node => {
            const pos = nodePositions[node.data.id];
            if (!pos) return null;

            const realId = node.data.supplier_id || node.data.mine_id || node.data.material_id || node.data.plant_id || node.data.vehicle_id || node.data.name || node.data.id;
            const isSelected = selectedEntityId === realId;

            return (
              <div
                key={node.data.id}
                onClick={(e) => {
                  e.stopPropagation();
                  if (onSelectEntity) onSelectEntity(realId, node.data.type || node.data.label || 'supplier');
                }}
                onMouseEnter={() => setHoveredNodeId(node.data.id)}
                onMouseLeave={() => setHoveredNodeId(null)}
                className={`absolute p-3 rounded-xl text-xs flex flex-col items-center border shadow-xl backdrop-blur-md cursor-pointer transition-all hover:scale-110 ${getNodeColor(node.data.type || '', isSelected)}`}
                style={{ left: pos.x, top: pos.y, transform: 'translate(-50%, -50%)' }}
                title={`Click to inspect entity: ${realId}`}
              >
                <span className="font-extrabold tracking-tight text-[11px]">{node.data.type || node.data.label}</span>
                <span className="text-[10px] opacity-90 max-w-[130px] truncate font-mono mt-0.5">
                  {node.data.name || realId}
                </span>
              </div>
            );
          })}
        </div>
      </div>

      <div className="flex flex-wrap gap-5 text-xs font-semibold text-muted-foreground mt-auto bg-background/40 p-3 rounded-xl border border-border/50">
        <span className="flex items-center gap-1.5"><span className="h-2.5 w-2.5 rounded-full bg-blue-500 shadow" /> Mines</span>
        <span className="flex items-center gap-1.5"><span className="h-2.5 w-2.5 rounded-full bg-sky-500 shadow" /> Suppliers</span>
        <span className="flex items-center gap-1.5"><span className="h-2.5 w-2.5 rounded-full bg-purple-500 shadow" /> Refineries</span>
        <span className="flex items-center gap-1.5"><span className="h-2.5 w-2.5 rounded-full bg-amber-500 shadow" /> Battery Plants</span>
        <span className="flex items-center gap-1.5"><span className="h-2.5 w-2.5 rounded-full bg-emerald-500 shadow" /> Fleet Vehicles</span>
      </div>
    </div>
  );
}
