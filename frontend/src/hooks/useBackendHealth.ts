import { useState, useEffect } from 'react'
import { HealthStatus } from '../types/dashboard'
import { apiService } from '../services/apiService'
import { APP_CONSTANTS } from '../constants/app.constants'

export function useBackendHealth(): HealthStatus {
  const [health, setHealth] = useState<HealthStatus>({
    status: 'pending',
    version: '0.1',
    backendConnected: null,
  })

  useEffect(() => {
    let isMounted = true

    const check = async () => {
      const result = await apiService.checkHealth()
      if (isMounted) {
        setHealth(result)
      }
    }

    check()
    const interval = setInterval(check, APP_CONSTANTS.HEALTH_POLL_INTERVAL_MS)

    return () => {
      isMounted = false
      clearInterval(interval)
    }
  }, [])

  return health
}
