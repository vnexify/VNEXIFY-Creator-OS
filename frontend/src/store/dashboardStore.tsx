import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react'
import { apiService } from '../services/apiService'
import { HealthStatus, ContentCardItem, ResearchItem, TaskItem, ProjectItem, AiStatus } from '../types/dashboard'
import { DASHBOARD_CONSTANTS } from '../constants/dashboard.constants'

export interface DashboardState {
  health: HealthStatus
  pipeline: ContentCardItem[]
  research: ResearchItem[]
  tasks: TaskItem[]
  recentProjects: ProjectItem[]
  aiStatus: AiStatus
  isLoading: boolean
  toggleTask: (id: string) => void
  refreshData: () => Promise<void>
}

const defaultState: DashboardState = {
  health: { status: 'pending', version: '0.1', backendConnected: null },
  pipeline: [],
  research: [],
  tasks: [],
  recentProjects: [],
  aiStatus: {
    provider: DASHBOARD_CONSTANTS.DEFAULT_AI_PROVIDER,
    activeModel: DASHBOARD_CONSTANTS.DEFAULT_AI_MODEL,
    status: 'Ready',
    ramUsage: '4.2 GB',
    contextWindow: DASHBOARD_CONSTANTS.DEFAULT_CONTEXT_WINDOW,
  },
  isLoading: true,
  toggleTask: () => {},
  refreshData: async () => {},
}

const DashboardContext = createContext<DashboardState>(defaultState)

export const DashboardProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [health, setHealth] = useState<HealthStatus>(defaultState.health)
  const [pipeline, setPipeline] = useState<ContentCardItem[]>([])
  const [research, setResearch] = useState<ResearchItem[]>([])
  const [tasks, setTasks] = useState<TaskItem[]>([])
  const [recentProjects, setRecentProjects] = useState<ProjectItem[]>([])
  const [isLoading, setIsLoading] = useState<boolean>(true)

  const refreshData = async () => {
    setIsLoading(true)
    try {
      const [h, p, r, t, proj] = await Promise.all([
        apiService.checkHealth(),
        apiService.fetchPipelineItems(),
        apiService.fetchResearchItems(),
        apiService.fetchTasks(),
        apiService.fetchRecentProjects(),
      ])

      setHealth(h)
      setPipeline(p)
      setResearch(r)
      setTasks(t)
      setRecentProjects(proj)
    } finally {
      setIsLoading(false)
    }
  }

  useEffect(() => {
    refreshData()
    const interval = setInterval(async () => {
      const h = await apiService.checkHealth()
      setHealth(h)
    }, 15000)

    return () => clearInterval(interval)
  }, [])

  const toggleTask = (id: string) => {
    setTasks((prev) =>
      prev.map((task) => (task.id === id ? { ...task, completed: !task.completed } : task))
    )
  }

  const contextValue: DashboardState = {
    health,
    pipeline,
    research,
    tasks,
    recentProjects,
    aiStatus: defaultState.aiStatus,
    isLoading,
    toggleTask,
    refreshData,
  }

  return (
    <DashboardContext.Provider value={contextValue}>
      {children}
    </DashboardContext.Provider>
  )
}

export const useDashboardStore = (): DashboardState => {
  return useContext(DashboardContext)
}
