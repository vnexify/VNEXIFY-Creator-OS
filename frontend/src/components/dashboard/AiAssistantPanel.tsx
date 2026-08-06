import React from 'react'
import { Icon } from '../common/Icon'
import { StatusBadge } from '../common/StatusBadge'

export const AiAssistantPanel: React.FC = () => {
  return (
    <section className="rounded-2xl border border-[#262b35] bg-[#16191e] p-5 shadow-lg">
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2">
          <Icon name="spark" className="h-4 w-4 text-[#7c3aed]" />
          <h3 className="text-sm font-semibold text-white">AI Assistant Status</h3>
        </div>
        <StatusBadge status="Ready" size="sm" />
      </div>

      <div className="mt-4 space-y-3">
        <div className="rounded-xl border border-[#262b35] bg-[#0d0f12] p-3 space-y-2 text-xs">
          <div className="flex items-center justify-between">
            <span className="text-slate-400">Default Provider:</span>
            <span className="font-semibold text-cyan-400">Ollama (Local)</span>
          </div>
          <div className="flex items-center justify-between">
            <span className="text-slate-400">Active Model:</span>
            <span className="font-mono text-slate-200">llama3:8b-instruct</span>
          </div>
          <div className="flex items-center justify-between">
            <span className="text-slate-400">Context Window:</span>
            <span className="font-mono text-slate-200">8,192 Tokens</span>
          </div>
        </div>

        <div className="flex gap-2">
          <button
            type="button"
            className="flex-1 rounded-lg border border-[#262b35] bg-[#0d0f12] py-2 text-center text-xs font-semibold text-slate-200 hover:border-[#7c3aed] hover:text-white"
          >
            Switch Model
          </button>
          <button
            type="button"
            className="flex-1 rounded-lg bg-gradient-to-r from-[#7c3aed] to-[#06b6d4] py-2 text-center text-xs font-semibold text-white hover:brightness-110"
          >
            Open Studio
          </button>
        </div>
      </div>
    </section>
  )
}
