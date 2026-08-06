import React from 'react'

interface StatusBadgeProps {
  status: 'Idea' | 'Draft' | 'Review' | 'Scheduled' | 'Published' | 'Connected' | 'Offline' | 'Pending' | string
  size?: 'sm' | 'md'
}

export const StatusBadge: React.FC<StatusBadgeProps> = ({ status, size = 'md' }) => {
  const getBadgeStyle = () => {
    switch (status) {
      case 'Published':
      case 'Connected':
        return 'bg-emerald-500/20 text-emerald-400 border-emerald-500/30'
      case 'Scheduled':
      case 'Review':
        return 'bg-amber-500/20 text-amber-400 border-amber-500/30'
      case 'Draft':
      case 'Pending':
        return 'bg-slate-500/20 text-slate-300 border-slate-500/30'
      case 'Idea':
        return 'bg-sky-500/20 text-sky-400 border-sky-500/30'
      case 'Offline':
        return 'bg-rose-500/20 text-rose-400 border-rose-500/30'
      default:
        return 'bg-violet-500/20 text-violet-300 border-violet-500/30'
    }
  }

  const padding = size === 'sm' ? 'px-2 py-0.5 text-[10px]' : 'px-2.5 py-1 text-xs'

  return (
    <span className={`inline-flex items-center gap-1.5 rounded-full border font-medium tracking-wide ${padding} ${getBadgeStyle()}`}>
      <span className="h-1.5 w-1.5 rounded-full bg-current" />
      {status}
    </span>
  )
}
