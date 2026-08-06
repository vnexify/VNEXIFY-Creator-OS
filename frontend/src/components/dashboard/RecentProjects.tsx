import React from 'react'
import { ProjectItem } from '../../types/dashboard'
import { StatusBadge } from '../common/StatusBadge'
import { formatWordCount } from '../../utils/formatters'

interface RecentProjectsProps {
  projects?: ProjectItem[]
}

export const RecentProjects: React.FC<RecentProjectsProps> = ({ projects = [] }) => {
  return (
    <section className="rounded-2xl border border-[#262b35] bg-[#16191e] p-5 shadow-lg">
      <div className="flex items-center justify-between">
        <h3 className="text-sm font-semibold text-white">Recent Projects</h3>
        <span className="text-xs text-slate-400">Context Resumption</span>
      </div>

      <div className="mt-4 overflow-x-auto">
        <table className="w-full text-left text-xs">
          <thead>
            <tr className="border-b border-[#262b35] text-[10px] font-bold uppercase tracking-wider text-slate-400">
              <th className="pb-2.5">Title</th>
              <th className="pb-2.5">Type</th>
              <th className="pb-2.5">Status</th>
              <th className="pb-2.5">Word Count</th>
              <th className="pb-2.5 text-right">Updated</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-[#262b35]/50">
            {projects.map((project) => (
              <tr key={project.id} className="group hover:bg-[#0d0f12]/50 transition cursor-pointer">
                <td className="py-3 font-semibold text-slate-200 group-hover:text-white">{project.title}</td>
                <td className="py-3 text-slate-400">{project.type}</td>
                <td className="py-3">
                  <StatusBadge status={project.status} size="sm" />
                </td>
                <td className="py-3 font-mono text-slate-400">{formatWordCount(project.wordCount)}</td>
                <td className="py-3 text-right text-slate-500">{project.updatedAt}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  )
}
