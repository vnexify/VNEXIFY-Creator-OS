import { backendClient } from '../api/client'
import { HealthStatus, ContentCardItem, ResearchItem, TaskItem, ProjectItem } from '../types/dashboard'
import { APP_CONSTANTS } from '../constants/app.constants'

export const apiService = {
  async checkHealth(): Promise<HealthStatus> {
    const response = await backendClient.get<{ status: string; version: string }>(APP_CONSTANTS.HEALTH_ENDPOINT)
    if (response.success && response.data && response.data.status === 'ok') {
      return {
        status: 'ok',
        version: response.data.version || '0.1',
        backendConnected: true,
      }
    }
    return {
      status: 'offline',
      version: '0.1',
      backendConnected: false,
    }
  },

  async fetchPipelineItems(): Promise<ContentCardItem[]> {
    const response = await backendClient.get<ContentCardItem[]>('/api/v1/content')
    if (response.success && Array.isArray(response.data)) {
      return response.data
    }
    return [
      { id: '1', title: 'Local-First AI Desktop Architecture', tag: 'Engineering', wordCount: 1450, stage: 'Draft', updatedAt: '12 mins ago' },
      { id: '2', title: 'Solopreneur Creator OS Guide', tag: 'Newsletter', wordCount: 2100, stage: 'Review', updatedAt: '2 hours ago' },
      { id: '3', title: 'SQLite WAL Mode Performance Benchmarks', tag: 'Database', wordCount: 950, stage: 'Idea', updatedAt: 'Yesterday' },
      { id: '4', title: 'Weekly Creator Tech Wrap-Up #42', tag: 'Publishing', wordCount: 650, stage: 'Scheduled', updatedAt: 'Today @ 4:00 PM' },
    ]
  },

  async fetchResearchItems(): Promise<ResearchItem[]> {
    const response = await backendClient.get<ResearchItem[]>('/api/v1/research/notes')
    if (response.success && Array.isArray(response.data)) {
      return response.data
    }
    return [
      { id: 'r1', title: 'SQLite WAL Mode Concurrent Benchmarks', sourceUrl: 'github.com/sqlite/benchmarks', category: 'Database', savedAt: '1 hour ago' },
      { id: 'r2', title: 'Desktop App Design Systems & Window Ergonomics', sourceUrl: 'uxdesign.cc/desktop-patterns', category: 'UI/UX', savedAt: 'Yesterday' },
      { id: 'r3', title: 'Local AI Model Quantization via Ollama', sourceUrl: 'ollama.com/library/llama3', category: 'AI Architecture', savedAt: '2 days ago' },
    ]
  },

  async fetchTasks(): Promise<TaskItem[]> {
    const response = await backendClient.get<TaskItem[]>('/api/v1/tasks')
    if (response.success && Array.isArray(response.data)) {
      return response.data
    }
    return [
      { id: 't1', title: 'Finalize outline for Local-First AI article', completed: true, priority: 'High' },
      { id: 't2', title: 'Draft script for YouTube Episode #14', completed: false, priority: 'High' },
      { id: 't3', title: 'Review thumbnail graphics in Media Library', completed: false, priority: 'Medium' },
      { id: 't4', title: 'Schedule Substack newsletter broadcast', completed: false, priority: 'Low' },
    ]
  },

  async fetchRecentProjects(): Promise<ProjectItem[]> {
    const response = await backendClient.get<ProjectItem[]>('/api/v1/content/recent')
    if (response.success && Array.isArray(response.data)) {
      return response.data
    }
    return [
      { id: 'p1', title: 'Building Local-First Desktop Systems', type: 'Article', status: 'Draft', wordCount: 1450, updatedAt: '12 mins ago' },
      { id: 'p2', title: 'Solopreneur Content Operations Guide', type: 'Newsletter', status: 'Review', wordCount: 2100, updatedAt: '2 hours ago' },
      { id: 'p3', title: 'Creator OS Architecture Overview', type: 'Video Script', status: 'Scheduled', wordCount: 3400, updatedAt: 'Yesterday' },
    ]
  },
}
