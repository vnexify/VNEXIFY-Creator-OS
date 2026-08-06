import React from 'react'
import { StatusBadge } from '../common/StatusBadge'

interface SystemHealthWidgetProps {
  backendConnected: boolean | null
}

export const SystemHealthWidget: React.FC<SystemHealthWidgetProps> = ({ backendConnected }) => {
  return (
    <section className="rounded-2xl border border-[#262b35] bg-[#16191e] p-5 shadow-lg">
      <div className="flex items-center justify-between">
        <h3 className="text-sm font-semibold text-white">System Health</h3>
        <StatusBadge status={backendConnected ? 'Connected' : 'Offline'} size="sm" />
      </div>

      <div className="mt-4 space-y-3 text-xs">
        <div className="rounded-xl border border-[#262b35] bg-[#0d0f12] p-3 flex items-center justify-between">
          <span className="text-slate-400">FastAPI Daemon</span>
          <span className="font-mono text-slate-200">{backendConnected ? '127.0.0.1:8000' : 'Disconnected'}</span>
        </div>
        <div className="rounded-xl border border-[#262b35] bg-[#0d0f12] p-3 flex items-center justify-between">
          <span className="text-slate-400">Electron Container</span>
          <span className="font-mono text-cyan-400">Active</span>
        </div>
      </div>
    </section>
  )
}
