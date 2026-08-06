import React from 'react'

interface StatusBarProps {
  backendConnected: boolean | null
}

export const StatusBar: React.FC<StatusBarProps> = ({ backendConnected }) => {
  return (
    <footer className="flex h-7 items-center justify-between border-t border-[#262b35] bg-[#0d0f12] px-4 text-[11px] font-mono text-slate-500 select-none">
      <div className="flex items-center gap-4">
        <span className="flex items-center gap-1.5">
          <span className={`h-2 w-2 rounded-full ${backendConnected ? 'bg-emerald-500 animate-pulse' : 'bg-rose-500'}`} />
          <span>Backend: {backendConnected ? '127.0.0.1:8000 (v0.1)' : 'Offline'}</span>
        </span>
        <span className="hidden sm:inline text-slate-600">|</span>
        <span className="hidden sm:inline">⚡ Ollama: Local Ready</span>
        <span className="hidden md:inline text-slate-600">|</span>
        <span className="hidden md:inline">💾 DB: SQLite (WAL)</span>
      </div>

      <div className="flex items-center gap-4">
        <span className="hidden lg:inline">⏱️ IPC Latency: 2ms</span>
        <span className="hidden lg:inline text-slate-600">|</span>
        <span>🧠 Memory: 184 MB</span>
        <span className="text-slate-600">|</span>
        <span>VNEXIFY Creator OS v0.1</span>
      </div>
    </footer>
  )
}
