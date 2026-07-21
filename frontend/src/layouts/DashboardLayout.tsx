import React, { useState } from "react";
import { Link, Outlet, useLocation } from "react-router-dom";
import {
  Truck,
  BatteryCharging,
  Share2,
  BellRing,
  Leaf,
  Menu,
  X,
  Gauge,
  User,
  SunMoon,
  Sliders,
} from "lucide-react";

export default function DashboardLayout() {
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const location = useLocation();

  const navigation = [
    { name: "Fleet Overview", href: "/", icon: Truck },
    { name: "Simulation Controller", href: "/simulator", icon: Sliders },
    { name: "Battery Analytics", href: "/battery", icon: BatteryCharging },
    { name: "Supply Chain Graph", href: "/supply-chain", icon: Share2 },
    { name: "System Alerts", href: "/alerts", icon: BellRing },
    { name: "Carbon Intelligence", href: "/carbon", icon: Leaf },
  ];


  return (
    <div className="min-h-screen flex bg-background text-foreground font-sans">
      {/* Sidebar Navigation */}
      <aside
        className={`fixed inset-y-0 left-0 z-50 w-64 bg-card border-r border-border transform ${
          sidebarOpen ? "translate-x-0" : "-translate-x-full"
        } lg:translate-x-0 lg:static transition-transform duration-300 ease-in-out flex flex-col justify-between`}
      >
        <div>
          {/* Sidebar Header */}
          <div className="h-16 px-6 border-b border-border flex items-center justify-between">
            <Link
              to="/"
              className="flex items-center gap-2 font-black tracking-wider text-lg uppercase text-blue-500"
            >
              <Gauge className="h-6 w-6" />
              <span>EV AI Platform</span>
            </Link>
            <button
              className="lg:hidden text-muted-foreground hover:text-foreground"
              onClick={() => setSidebarOpen(false)}
            >
              <X className="h-5 w-5" />
            </button>
          </div>

          {/* Navigation Links */}
          <nav className="p-4 space-y-1.5">
            {navigation.map((item) => {
              const active = location.pathname === item.href;
              const Icon = item.icon;
              return (
                <Link
                  key={item.name}
                  to={item.href}
                  onClick={() => setSidebarOpen(false)}
                  className={`flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm font-semibold transition-all ${
                    active
                      ? "bg-blue-500/10 text-blue-400 border-l-2 border-blue-500"
                      : "text-muted-foreground hover:bg-muted/30 hover:text-foreground"
                  }`}
                >
                  <Icon className="h-4.5 w-4.5 shrink-0" />
                  <span>{item.name}</span>
                </Link>
              );
            })}
          </nav>
        </div>

        {/* Sidebar Footer */}
        <div className="p-4 border-t border-border flex items-center justify-between text-xs text-muted-foreground">
          <span>Version 1.0.0-Beta</span>
          <span>© 2026 EV AI Inc.</span>
        </div>
      </aside>

      {/* Main Content Area */}
      <div className="flex-1 flex flex-col min-w-0 overflow-y-auto">
        {/* Top Navbar */}
        <header className="h-16 border-b border-border bg-card/50 backdrop-blur-md sticky top-0 z-40 flex items-center justify-between px-6">
          <div className="flex items-center gap-3">
            <button
              className="lg:hidden text-muted-foreground hover:text-foreground p-1"
              onClick={() => setSidebarOpen(true)}
            >
              <Menu className="h-5 w-5" />
            </button>
            <div className="hidden sm:block text-xs font-semibold text-muted-foreground bg-muted/40 px-2.5 py-1 rounded border border-border">
              Cluster Status:{" "}
              <span className="text-emerald-500">OPERATIONAL</span>
            </div>
          </div>

          <div className="flex items-center gap-4">
            {/* Quick action buttons */}
            <button className="p-2 text-muted-foreground hover:text-foreground hover:bg-muted/50 rounded-lg transition-colors">
              <SunMoon className="h-5 w-5" />
            </button>
            <div className="h-4 w-[1px] bg-border" />
            <div className="flex items-center gap-2.5">
              <div className="h-8 w-8 rounded-lg bg-blue-500/10 border border-blue-500/20 text-blue-500 flex items-center justify-center font-bold text-sm">
                A1
              </div>
              <span className="hidden md:block text-sm font-semibold">
                Hackathon User
              </span>
            </div>
          </div>
        </header>

        {/* Page Inner Container */}
        <main className="p-6 md:p-8 max-w-7xl w-full mx-auto">
          <Outlet />
        </main>
      </div>
    </div>
  );
}
