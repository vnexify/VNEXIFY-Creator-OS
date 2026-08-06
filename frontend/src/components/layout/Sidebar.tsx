import React, { useState } from 'react'
import { Icon } from '../common/Icon'
import { NavigationItem } from '../../types/dashboard'

interface SidebarProps {
  activeModule: string
  onSelectModule: (id: string) => void
}

export const Sidebar: React.FC<SidebarProps> = ({ activeModule, onSelectModule }) => {
  const [collapsed, setCollapsed] = useState(false)

  const modules: NavigationItem[] = [
    { id: 'dashboard', label: 'Dashboard', icon: 'dashboard' },
    { id: 'research', label: 'Research', icon: 'research' },
    { id: 'content', label: 'Content', icon: 'content' },
    { id: 'ai', label: 'AI Studio', icon: 'spark' },
    { id: 'analytics', label: 'Analytics', icon: 'analytics' },
    { id: 'calendar', label: 'Calendar', icon: 'calendar' },
    { id: 'media', label: 'Media', icon: 'media' },
    { id: 'settings', label: 'Settings', icon: 'settings' },
  ]

  return (
    <aside
      className={`flex flex-col border-r border-[#262b35] bg-[#0f1115] transition-all duration-200 ${
        collapsed ? 'w-16' : 'w-60'
      }`}
    >
      <div className="p-3">
        <div
          className={`rounded-xl border border-[#262b35] bg-gradient-to-br from-[#7c3aed]/15 to-[#06b6d4]/10 p-3 ${
            collapsed ? 'text-center' : ''
          }`}
        >
          {!collapsed ? (
            <>
              <p className="text-[10px] font-semibold uppercase tracking-[0.25em] text-slate-400">Workspace</p>
              <h2 className="mt-1 text-sm font-bold text-white">Main Studio</h2>
              <p className="text-[11px] text-slate-400">Local-First Desktop OS</p>
            </>
          ) : (
            <div className="flex justify-center">
              <Icon name="spark" className="h-5 w-5 text-[#7c3aed]" />
            </div>
          )}
        </div>
      </div>

      <nav className="flex-1 space-y-1 p-2 overflow-y-auto">
        {modules.map((item) => {
          const isActive = activeModule === item.id
          return (
            <button
              key={item.id}
              type="button"
              onClick={() => onSelectModule(item.id)}
              title={collapsed ? item.label : undefined}
              className={`flex w-full items-center gap-3 rounded-lg px-3 py-2 text-xs font-medium transition ${
                isActive
                  ? 'bg-[#1f232b] text-white shadow-sm ring-1 ring-[#7c3aed]/40'
                  : 'text-slate-400 hover:bg-[#16191e] hover:text-slate-200'
              }`}
            >
              <span
                className={`rounded-md p-1.5 transition ${
                  isActive ? 'bg-[#7c3aed]/20 text-[#7c3aed]' : 'bg-[#16191e] text-slate-400'
                }`}
              >
                <Icon name={item.icon} className="h-4 w-4" />
              </span>
              {!collapsed && <span>{item.label}</span>}
            </button>
          )
        })}
      </nav>

      <div className="border-t border-[#262b35] p-2">
        <button
          type="button"
          onClick={() => setCollapsed(!collapsed)}
          className="flex w-full items-center justify-center rounded-lg border border-[#262b35] bg-[#16191e] py-1.5 text-xs text-slate-400 hover:text-white"
        >
          {collapsed ? '→' : '← Collapse'}
        </button>
      </div>
    </aside>
  )
}
