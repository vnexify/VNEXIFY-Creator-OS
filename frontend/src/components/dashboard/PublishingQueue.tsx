import React from 'react'
import { Icon } from '../common/Icon'

export const PublishingQueue: React.FC = () => {
  const queuedReleases = [
    { channel: 'Substack', title: 'Weekly Tech Recap #42', time: 'Today @ 4:00 PM' },
    { channel: 'YouTube', title: 'Local AI Deep Dive Episode', time: 'Tomorrow @ 10:00 AM' },
  ]

  return (
    <section className="rounded-2xl border border-[#262b35] bg-[#16191e] p-5 shadow-lg">
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2">
          <Icon name="spark" className="h-4 w-4 text-emerald-400" />
          <h3 className="text-sm font-semibold text-white">Publishing Queue</h3>
        </div>
        <span className="rounded-full border border-[#262b35] bg-[#0d0f12] px-2 py-0.5 text-[10px] text-slate-400">
          2 Queued
        </span>
      </div>

      <div className="mt-4 space-y-2">
        {queuedReleases.map((item) => (
          <div key={item.title} className="rounded-xl border border-[#262b35] bg-[#0d0f12] p-3 text-xs">
            <div className="flex items-center justify-between">
              <span className="font-semibold text-emerald-400">[{item.channel}]</span>
              <span className="text-[10px] text-slate-400 font-mono">{item.time}</span>
            </div>
            <p className="mt-1 text-slate-200">{item.title}</p>
          </div>
        ))}
      </div>
    </section>
  )
}
