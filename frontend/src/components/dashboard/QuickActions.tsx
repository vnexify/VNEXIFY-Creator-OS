import React from 'react'
import { Icon } from '../common/Icon'

interface QuickActionsProps {
  onActionClick?: (actionId: string) => void
}

export const QuickActions: React.FC<QuickActionsProps> = ({ onActionClick }) => {
  const actions = [
    { id: 'new-draft', label: 'New Content Draft', icon: 'content', color: 'from-violet-500/20 to-purple-500/10' },
    { id: 'ai-prompt', label: 'Run AI Prompt Studio', icon: 'spark', color: 'from-cyan-500/20 to-blue-500/10' },
    { id: 'clip-research', label: 'Clip Web Research', icon: 'research', color: 'from-emerald-500/20 to-teal-500/10' },
    { id: 'import-media', label: 'Import Media Asset', icon: 'media', color: 'from-amber-500/20 to-orange-500/10' },
    { id: 'compile-export', label: 'Compile Export Bundle', icon: 'analytics', color: 'from-pink-500/20 to-rose-500/10' },
    { id: 'view-calendar', label: 'View Schedule Grid', icon: 'calendar', color: 'from-sky-500/20 to-indigo-500/10' },
  ]

  return (
    <section className="rounded-2xl border border-[#262b35] bg-[#16191e] p-5 shadow-lg">
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2">
          <Icon name="spark" className="h-4 w-4 text-[#7c3aed]" />
          <h3 className="text-sm font-semibold text-white">Quick Actions</h3>
        </div>
        <span className="rounded-full border border-[#262b35] bg-[#0d0f12] px-2.5 py-0.5 text-[10px] uppercase tracking-wider text-slate-400">
          Fast Access
        </span>
      </div>

      <div className="mt-4 grid grid-cols-2 gap-3 lg:grid-cols-3">
        {actions.map((action) => (
          <button
            key={action.id}
            type="button"
            onClick={() => onActionClick?.(action.id)}
            className="group flex flex-col justify-between rounded-xl border border-[#262b35] bg-[#0d0f12] p-3.5 text-left transition hover:border-[#7c3aed] hover:bg-[#1f232b] active:scale-[0.99]"
          >
            <div className={`mb-3 inline-flex h-8 w-8 items-center justify-center rounded-lg bg-gradient-to-br ${action.color} border border-[#262b35]`}>
              <Icon name={action.icon} className="h-4 w-4 text-slate-200 transition group-hover:text-white" />
            </div>
            <span className="text-xs font-semibold text-slate-200 group-hover:text-white">{action.label}</span>
          </button>
        ))}
      </div>
    </section>
  )
}
