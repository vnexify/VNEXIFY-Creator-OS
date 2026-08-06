export function generateUniqueId(prefix = 'id'): string {
  return `${prefix}_${Math.random().toString(36).substring(2, 9)}`
}

export function getStatusBadgeStyle(status: string): string {
  switch (status) {
    case 'Published':
    case 'Connected':
    case 'ok':
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
    case 'Error':
      return 'bg-rose-500/20 text-rose-400 border-rose-500/30'
    default:
      return 'bg-violet-500/20 text-violet-300 border-violet-500/30'
  }
}
