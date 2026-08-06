import React, { useState } from 'react'
import { Header } from '../components/layout/Header'
import { Sidebar } from '../components/layout/Sidebar'
import { StatusBar } from '../components/layout/StatusBar'
import { WelcomeCard } from '../components/dashboard/WelcomeCard'
import { QuickActions } from '../components/dashboard/QuickActions'
import { MetricKpiCard } from '../components/cards/MetricKpiCard'
import { ContentPipeline } from '../components/dashboard/ContentPipeline'
import { RecentProjects } from '../components/dashboard/RecentProjects'
import { TaskCard } from '../components/dashboard/TaskCard'
import { AiAssistantPanel } from '../components/dashboard/AiAssistantPanel'
import { ResearchQueue } from '../components/dashboard/ResearchQueue'
import { CalendarPreview } from '../components/dashboard/CalendarPreview'
import { PublishingQueue } from '../components/dashboard/PublishingQueue'
import { SystemHealthWidget } from '../components/dashboard/SystemHealthWidget'
import { DashboardProvider, useDashboardStore } from '../store/dashboardStore'

const DashboardContent: React.FC = () => {
  const [activeModule, setActiveModule] = useState('dashboard')
  const { health, pipeline, research, tasks, recentProjects, toggleTask } = useDashboardStore()

  return (
    <div className="flex h-screen w-screen flex-col overflow-hidden bg-[#0d0f12] text-[#f8fafc] select-none">
      <Header backendConnected={health.backendConnected} />

      <div className="flex flex-1 overflow-hidden">
        <Sidebar activeModule={activeModule} onSelectModule={setActiveModule} />

        <main className="flex-1 overflow-y-auto bg-[radial-gradient(circle_at_top_left,_rgba(6,182,212,0.08),_transparent_30%),linear-gradient(135deg,_rgba(124,58,237,0.05),_transparent)] p-6">
          <div className="mx-auto flex max-w-7xl flex-col gap-6">
            <WelcomeCard />

            <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
              <MetricKpiCard title="Active Draft Pipeline" value={pipeline.length} trend="+12%" subtext="+2 added this week" />
              <MetricKpiCard title="Upcoming Scheduled" value={4} subtext="Next release: Today @ 4:00 PM" />
              <MetricKpiCard title="Monthly Velocity" value={28} trend="+18%" subtext="Published content items" />
              <MetricKpiCard title="AI Token Usage" value="142.5k" subtext="85% via Local Ollama" />
            </div>

            <div className="grid grid-cols-1 gap-6 lg:grid-cols-3">
              <div className="lg:col-span-2 space-y-6">
                <ContentPipeline items={pipeline} />
                <QuickActions />
                <RecentProjects projects={recentProjects} />
              </div>

              <div className="space-y-6">
                <AiAssistantPanel />
                <TaskCard tasks={tasks} onToggleTask={toggleTask} />
                <ResearchQueue items={research} />
                <PublishingQueue />
                <CalendarPreview />
                <SystemHealthWidget backendConnected={health.backendConnected} />
              </div>
            </div>
          </div>
        </main>
      </div>

      <StatusBar backendConnected={health.backendConnected} />
    </div>
  )
}

export const DashboardPage: React.FC = () => {
  return (
    <DashboardProvider>
      <DashboardContent />
    </DashboardProvider>
  )
}
