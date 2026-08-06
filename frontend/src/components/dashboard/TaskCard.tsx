import React from 'react'
import { TaskItem } from '../../types/dashboard'
import { Icon } from '../common/Icon'
import { getStatusBadgeStyle } from '../../utils/helpers'

interface TaskCardProps {
  tasks?: TaskItem[]
  onToggleTask?: (id: string) => void
}

export const TaskCard: React.FC<TaskCardProps> = ({ tasks = [], onToggleTask }) => {
  const completedCount = tasks.filter((t) => t.completed).length

  return (
    <section className="rounded-2xl border border-[#262b35] bg-[#16191e] p-5 shadow-lg">
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2">
          <Icon name="check" className="h-4 w-4 text-emerald-400" />
          <h3 className="text-sm font-semibold text-white">Today's Tasks</h3>
        </div>
        <span className="rounded-full border border-[#262b35] bg-[#0d0f12] px-2 py-0.5 text-[10px] font-mono text-slate-400">
          {completedCount} / {tasks.length} Done
        </span>
      </div>

      <div className="mt-4 space-y-2">
        {tasks.map((task) => (
          <button
            key={task.id}
            type="button"
            onClick={() => onToggleTask?.(task.id)}
            className="flex w-full items-center justify-between rounded-xl border border-[#262b35] bg-[#0d0f12] p-3 text-left transition hover:border-[#7c3aed]"
          >
            <div className="flex items-center gap-3">
              <span
                className={`flex h-4 w-4 items-center justify-center rounded border transition ${
                  task.completed
                    ? 'border-emerald-500 bg-emerald-500 text-black'
                    : 'border-[#262b35] bg-[#16191e]'
                }`}
              >
                {task.completed && <Icon name="check" className="h-3 w-3" />}
              </span>
              <span
                className={`text-xs ${
                  task.completed ? 'text-slate-500 line-through' : 'text-slate-200'
                }`}
              >
                {task.title}
              </span>
            </div>
            <span
              className={`rounded px-1.5 py-0.5 text-[9px] font-semibold uppercase ${getStatusBadgeStyle(
                task.priority
              )}`}
            >
              {task.priority}
            </span>
          </button>
        ))}
      </div>
    </section>
  )
}
