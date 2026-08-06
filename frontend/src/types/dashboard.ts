export interface NavigationItem {
  id: string
  label: string
  icon: string
  active?: boolean
  badge?: string
}

export interface ContentCardItem {
  id: string
  title: string
  tag: string
  wordCount: number
  stage: 'Idea' | 'Draft' | 'Review' | 'Scheduled' | 'Published'
  updatedAt: string
}

export interface ResearchItem {
  id: string
  title: string
  sourceUrl: string
  category: string
  savedAt: string
}

export interface TaskItem {
  id: string
  title: string
  completed: boolean
  priority: 'High' | 'Medium' | 'Low'
}

export interface ProjectItem {
  id: string
  title: string
  type: string
  status: 'Draft' | 'Review' | 'Scheduled' | 'Published'
  wordCount: number
  updatedAt: string
}

export interface AiStatus {
  provider: string
  activeModel: string
  status: 'Ready' | 'Connecting' | 'Offline'
  ramUsage: string
  contextWindow: number
}

export interface HealthStatus {
  status: string
  version: string
  backendConnected: boolean | null
}
