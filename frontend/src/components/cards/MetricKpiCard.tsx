import React from 'react'

interface MetricKpiCardProps {
  title: string
  value: string | number
  subtext: string
  trend?: string
}

export const MetricKpiCard: React.FC<MetricKpiCardProps> = ({ title, value, subtext, trend }) => {
  return (
    <div className="rounded-2xl border border-[#262b35] bg-[#16191e] p-5 shadow-lg flex flex-col justify-between">
      <p className="text-[11px] font-bold uppercase tracking-wider text-slate-400">{title}</p>
      <div className="mt-2 flex items-baseline justify-between">
        <span className="text-2xl font-bold tracking-tight text-white">{value}</span>
        {trend && <span className="text-xs font-semibold text-emerald-400">{trend}</span>}
      </div>
      <p className="mt-2 text-xs text-slate-400 font-mono">{subtext}</p>
    </div>
  )
}
