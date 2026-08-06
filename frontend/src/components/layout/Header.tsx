import React from 'react'
import { Icon } from '../common/Icon'

interface HeaderProps {
  backendConnected: boolean | null
  onNewContent?: () => void
}

export const Header: React.FC<HeaderProps> = ({ backendConnected, onNewContent }) => {
  return (
    <header className="flex h-14 items-center justify-between border-b border-[#262b35] bg-[#0d0f12]/95 px-6 select-none">
      <div className="flex items-center gap-3">
        <div className="flex h-9 w-9 items-center justify-center rounded-xl bg-gradient-to-br from-[#7c3aed] to-[#06b6d4] shadow-md shadow-violet-950/40">
          <Icon name="spark" className="h-5 w-5 text-white" />
        </div>
        <div>
          <h1 className="text-base font-bold tracking-tight text-white">VNEXIFY Creator OS</h1>
          <p className="text-xs text-slate-400">Desktop Workspace · v0.1</p>
        </div>
      </div>

      <div className="flex items-center gap-3">
        <div className="hidden items-center gap-2 rounded-lg border border-[#262b35] bg-[#16191e] px-3 py-1.5 text-xs text-slate-400 md:flex">
          <Icon name="search" className="h-3.5 w-3.5 text-slate-400" />
          <span>Search workspace</span>
          <kbd className="rounded border border-[#262b35] bg-[#0d0f12] px-1.5 py-0.5 text-[10px] font-mono text-slate-400">
            ⌘K
          </kbd>
        </div>

        <div className="flex items-center gap-2 rounded-lg border border-[#262b35] bg-[#16191e] px-3 py-1.5 text-xs">
          <span className="text-slate-400">Backend:</span>
          {backendConnected === null ? (
            <span className="font-medium text-amber-400">Connecting...</span>
          ) : backendConnected ? (
            <span className="font-medium text-emerald-400">🟢 127.0.0.1:8000</span>
          ) : (
            <span className="font-medium text-rose-400">🔴 Offline</span>
          )}
        </div>

        <button
          type="button"
          onClick={onNewContent}
          className="flex items-center gap-1.5 rounded-lg bg-gradient-to-r from-[#7c3aed] to-[#06b6d4] px-3.5 py-1.5 text-xs font-semibold text-white shadow-md shadow-violet-950/30 transition hover:brightness-110 active:scale-[0.98]"
        >
          <Icon name="plus" className="h-4 w-4" />
          <span>New Content</span>
        </button>
      </div>
    </header>
  )
}
