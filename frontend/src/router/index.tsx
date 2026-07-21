import React from 'react';
import { createBrowserRouter } from 'react-router-dom';
import DashboardLayout from '../layouts/DashboardLayout';
import FleetOverview from '../pages/FleetOverview';
import BatteryAnalytics from '../pages/BatteryAnalytics';
import SupplyChain from '../pages/SupplyChain';
import Alerts from '../pages/Alerts';
import CarbonAnalytics from '../pages/CarbonAnalytics';
import SimulationController from '../pages/SimulationController';

export const router = createBrowserRouter([
  {
    path: '/',
    element: <DashboardLayout />,
    children: [
      {
        index: true,
        element: <FleetOverview />,
      },
      {
        path: 'battery',
        element: <BatteryAnalytics />,
      },
      {
        path: 'supply-chain',
        element: <SupplyChain />,
      },
      {
        path: 'alerts',
        element: <Alerts />,
      },
      {
        path: 'carbon',
        element: <CarbonAnalytics />,
      },
      {
        path: 'simulator',
        element: <SimulationController />,
      },
    ],
  },
], {
  future: {
    v7_startTransition: true,
    v7_relativeSplatPath: true,
  },
});

