import React from 'react'
import { Icon } from '../common/Icon'
import { ResearchItem } from '../../types/dashboard'

interface ResearchQueueProps {
  items?: ResearchItem[]
}

export const ResearchQueue: React.FC<ResearchQueueProps> = ({ items = [] }) => {
  const defaultItems: ResearchItem[] = [
    { id: 'r1', title: 'SQLite WAL Mode Concurrent Benchmarks', sourceUrl: 'github.com/sqlite/benchmarks', category: 'Database', savedAt: '1 hour ago' },
    { id: 'r2', title: 'Desktop App Design Systems & Window Ergonomics', sourceUrl: 'uxdesign.cc/desktop-patterns', category: 'UI/UX', savedAt: 'Yesterday' },
    { id: 'r3', title: 'Local AI Model Quantization via Ollama', sourceUrl: 'ollama.com/library/llama3', category: 'AI Architecture', savedAt: '2 days ago' },
  ]

  const displayItems = items.length > 0 ? items : defaultItems

  return (
    <section className="rounded-2xl border border-[#262b35] bg-[#16191e] p-5 shadow-lg">
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2">
          <Icon name="research" className="h-4 w-4 text-[#06b6d4]" />
          <h3 className="text-sm font-semibold text-white">Research Queue</h3>
        </div>
        <span className="rounded-full border border-[#262b35] bg-[#0d0f12] px-2 py-0.5 text-[10px] text-slate-400">
          {displayItems.length} Clips
        </span>
      </div>

      <div className="mt-4 space-y-2.5">
        {displayItems.map((item) => (
          <div
            key={item.id}
            className="group rounded-xl border border-[#262b35] bg-[#0d0f12] p-3 transition hover:border-[#06b6d4]"
          >
            <div className="flex items-start justify-between gap-2">
              <p className="text-xs font-semibold text-slate-200 group-hover:text-white line-clamp-1">
                📌 {item.title}
              </p>
            </div>
            <div className="mt-2 flex items-center justify-between text-[10px] text-slate-400">
              <span className="font-mono text-slate-500">{item.sourceUrl}</span>
              <span className="rounded bg-[#16191e] px-1.5 py-0.5 text-[#06b6d4]">{item.category}</span>
            </div>
          </div>
        ))}
      </div>
    </section>
  )
}
