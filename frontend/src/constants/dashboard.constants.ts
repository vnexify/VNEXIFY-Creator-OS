export const DASHBOARD_CONSTANTS = {
  STAGES: ['Idea', 'Draft', 'Review', 'Scheduled', 'Published'] as const,
  PRIORITIES: ['High', 'Medium', 'Low'] as const,
  DEFAULT_AI_PROVIDER: 'Ollama (Local)',
  DEFAULT_AI_MODEL: 'llama3:8b-instruct',
  DEFAULT_CONTEXT_WINDOW: 8192,
} as const
