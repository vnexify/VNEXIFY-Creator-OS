import React from 'react'
import { Icon } from '../common/Icon'

export const CalendarPreview: React.FC = () => {
  return (
    <section className="rounded-2xl border border-[#262b35] bg-[#16191e] p-5 shadow-lg">
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2">
          <Icon name="calendar" className="h-4 w-4 text-[#06b6d4]" />
          <h3 className="text-sm font-semibold text-white">Calendar Preview</h3>
        </div>
        <span className="text-xs font-mono text-slate-400">August 2026</span>
      </div>

      <div className="mt-4 rounded-xl border border-[#262b35] bg-[#0d0f12] p-3 text-center text-xs">
        <div className="grid grid-cols-7 gap-1 font-mono text-[10px] font-bold text-slate-500 mb-2">
          <span>SU</span><span>MO</span><span>TU</span><span>WE</span><span>TH</span><span>FR</span><span>SA</span>
        </div>
        <div className="grid grid-cols-7 gap-1 font-mono text-slate-300">
          <span className="text-slate-600">2</span>
          <span className="text-slate-600">3</span>
          <span className="text-slate-600">4</span>
          <span className="text-slate-600">5</span>
          <span className="rounded bg-[#7c3aed] text-white font-bold">6*</span>
          <span>7</span>
          <span>8</span>
        </div>
        <div className="mt-3 border-t border-[#262b35] pt-2.5 text-left text-[11px]">
          <p className="font-semibold text-slate-200">Next Release:</p>
          <p className="text-slate-400">Substack: Creator OS Deep Dive @ 4:00 PM</p>
        </div>
      </div>
    </section>
  )
}
