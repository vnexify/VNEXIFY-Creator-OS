import { APP_CONSTANTS } from '../constants/app.constants'

export interface ApiResponse<T = unknown> {
  success: boolean
  data?: T
  error?: {
    code: string
    message: string
  }
}

class BackendClient {
  private baseUrl: string

  constructor(baseUrl: string = APP_CONSTANTS.DEFAULT_BACKEND_URL) {
    this.baseUrl = baseUrl
  }

  public async get<T>(endpoint: string): Promise<ApiResponse<T>> {
    try {
      const controller = new AbortController()
      const timeoutId = setTimeout(() => controller.abort(), APP_CONSTANTS.REQUEST_TIMEOUT_MS)

      const response = await fetch(`${this.baseUrl}${endpoint}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
        },
        signal: controller.signal,
      })

      clearTimeout(timeoutId)

      if (!response.ok) {
        return {
          success: false,
          error: {
            code: `HTTP_${response.status}`,
            message: `Request failed with status ${response.status}`,
          },
        }
      }

      const data = await response.json()
      return {
        success: true,
        data,
      }
    } catch (err) {
      return {
        success: false,
        error: {
          code: 'NETWORK_ERROR',
          message: err instanceof Error ? err.message : 'Failed to connect to backend',
        },
      }
    }
  }

  public async post<T>(endpoint: string, body: unknown): Promise<ApiResponse<T>> {
    try {
      const response = await fetch(`${this.baseUrl}${endpoint}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
        },
        body: JSON.stringify(body),
      })

      if (!response.ok) {
        return {
          success: false,
          error: {
            code: `HTTP_${response.status}`,
            message: `POST failed with status ${response.status}`,
          },
        }
      }

      const data = await response.json()
      return {
        success: true,
        data,
      }
    } catch (err) {
      return {
        success: false,
        error: {
          code: 'NETWORK_ERROR',
          message: err instanceof Error ? err.message : 'Network connection error',
        },
      }
    }
  }
}

export const backendClient = new BackendClient()
