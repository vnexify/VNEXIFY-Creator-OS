import React from 'react'
import { StatusBadge } from '../common/StatusBadge'
import { ContentCardItem } from '../../types/dashboard'
import { formatWordCount } from '../../utils/formatters'
import { DASHBOARD_CONSTANTS } from '../../constants/dashboard.constants'

interface ContentPipelineProps {
  items?: ContentCardItem[]
}

export const ContentPipeline: React.FC<ContentPipelineProps> = ({ items = [] }) => {
  const displayItems = items
  const stages = DASHBOARD_CONSTANTS.STAGES.filter((stage) => stage !== 'Published')

  return (
    <section className="rounded-2xl border border-[#262b35] bg-[#16191e] p-5 shadow-lg">
      <div className="flex items-center justify-between">
        <div>
          <h3 className="text-sm font-semibold text-white">Content Pipeline</h3>
          <p className="text-xs text-slate-400">Lifecycle stage board (Idea ➔ Published)</p>
        </div>
        <span className="rounded-full border border-[#262b35] bg-[#0d0f12] px-2.5 py-0.5 text-[10px] uppercase tracking-wider text-slate-400">
          Kanban View
        </span>
      </div>

      <div className="mt-4 grid grid-cols-1 gap-3 sm:grid-cols-2 lg:grid-cols-4">
        {stages.map((stage) => {
          const stageItems = displayItems.filter((item) => item.stage === stage)
          return (
            <div key={stage} className="rounded-xl border border-[#262b35] bg-[#0d0f12] p-3 flex flex-col gap-2">
              <div className="flex items-center justify-between border-b border-[#262b35] pb-2">
                <span className="text-xs font-bold text-slate-300">{stage}</span>
                <span className="rounded-full bg-[#16191e] px-2 py-0.5 text-[10px] font-mono text-slate-400">
                  {stageItems.length}
                </span>
              </div>

              <div className="flex flex-col gap-2 mt-1 min-h-[120px]">
                {stageItems.length > 0 ? (
                  stageItems.map((item) => (
                    <div
                      key={item.id}
                      className="rounded-lg border border-[#262b35] bg-[#16191e] p-3 hover:border-[#7c3aed] transition cursor-pointer"
                    >
                      <p className="text-xs font-semibold text-white line-clamp-2">{item.title}</p>
                      <div className="mt-2 flex items-center justify-between text-[10px]">
                        <StatusBadge status={item.stage} size="sm" />
                        <span className="text-slate-400 font-mono">{formatWordCount(item.wordCount)}</span>
                      </div>
                    </div>
                  ))
                ) : (
                  <div className="flex h-full items-center justify-center rounded-lg border border-dashed border-[#262b35] p-4 text-[10px] text-slate-500">
                    No items in {stage}
                  </div>
                )}
              </div>
            </div>
          )
        })}
      </div>
    </section>
  )
}
