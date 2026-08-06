import React from 'react'
import { Icon } from '../common/Icon'

interface WelcomeCardProps {
  onNewContent?: () => void
  onOpenResearch?: () => void
}

export const WelcomeCard: React.FC<WelcomeCardProps> = ({ onNewContent, onOpenResearch }) => {
  return (
    <section className="relative overflow-hidden rounded-2xl border border-[#262b35] bg-gradient-to-r from-[#16191e] via-[#16191e] to-[#1f232b] p-6 shadow-xl">
      <div className="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
        <div className="space-y-2">
          <div className="inline-flex items-center gap-2 rounded-full border border-[#262b35] bg-[#0d0f12] px-3 py-1 text-[11px] font-medium uppercase tracking-[0.2em] text-[#06b6d4]">
            <Icon name="spark" className="h-3.5 w-3.5" />
            <span>Workspace Active</span>
          </div>
          <h2 className="text-2xl font-bold tracking-tight text-white">Welcome back, Creator</h2>
          <p className="max-w-xl text-xs leading-relaxed text-slate-400">
            Your local-first desktop workspace is connected. Track content velocity, refine research clips, and execute multi-model AI prompts in calm focus.
          </p>
        </div>

        <div className="flex flex-wrap gap-3">
          <button
            type="button"
            onClick={onOpenResearch}
            className="flex items-center gap-2 rounded-xl border border-[#262b35] bg-[#0d0f12] px-4 py-2.5 text-xs font-semibold text-slate-200 transition hover:border-[#06b6d4] hover:text-white"
          >
            <Icon name="research" className="h-4 w-4 text-[#06b6d4]" />
            <span>Research Queue</span>
          </button>
          <button
            type="button"
            onClick={onNewContent}
            className="flex items-center gap-2 rounded-xl bg-gradient-to-r from-[#7c3aed] to-[#06b6d4] px-4 py-2.5 text-xs font-semibold text-white shadow-lg shadow-violet-950/40 transition hover:brightness-110"
          >
            <Icon name="plus" className="h-4 w-4" />
            <span>+ Create Draft</span>
          </button>
        </div>
      </div>
    </section>
  )
}
