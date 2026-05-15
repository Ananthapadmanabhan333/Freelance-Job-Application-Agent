"use client";

import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { 
  Radar, 
  Terminal, 
  Target, 
  Zap, 
  Shield, 
  BarChart3, 
  Briefcase, 
  ChevronRight,
  Search,
  CheckCircle2,
  AlertCircle
} from 'lucide-react';

const OpportunityCard = ({ job, index }: { job: any, index: number }) => (
  <motion.div
    initial={{ opacity: 0, x: -20 }}
    animate={{ opacity: 1, x: 0 }}
    transition={{ delay: index * 0.1 }}
    className="glass-card p-4 mb-4 group cursor-pointer hover:border-primary/50 transition-all"
  >
    <div className="flex justify-between items-start mb-2">
      <h3 className="text-lg font-semibold text-primary group-hover:text-secondary transition-colors">{job.title}</h3>
      <div className="flex items-center gap-2">
        <span className="text-xs px-2 py-1 rounded-full bg-primary/10 text-primary border border-primary/20">
          {job.score}% Match
        </span>
        <span className="text-xs px-2 py-1 rounded-full bg-green-500/10 text-green-500 border border-green-500/20">
          ${job.budget}
        </span>
      </div>
    </div>
    <p className="text-sm text-gray-400 line-clamp-2 mb-4">{job.description}</p>
    <div className="flex justify-between items-center text-xs text-gray-500">
      <div className="flex gap-4">
        <span className="flex items-center gap-1"><Search size={12} /> {job.platform}</span>
        <span className="flex items-center gap-1"><Briefcase size={12} /> {job.type}</span>
      </div>
      <button className="flex items-center gap-1 text-primary hover:text-white transition-colors">
        Analyze <ChevronRight size={14} />
      </button>
    </div>
  </motion.div>
);

export default function Dashboard() {
  const [logs, setLogs] = useState<string[]>(["[SYSTEM] Initializing Lumina OS...", "[NETWORK] Discovery agents online.", "[AI] Analyzing current market trends..."]);
  const [jobs, setJobs] = useState<any[]>([]);
  const [isSwarming, setIsSwarming] = useState(false);

  useEffect(() => {
    const fetchJobs = async () => {
      try {
        const res = await fetch('http://localhost:8000/jobs');
        const data = await res.json();
        if (data && data.length > 0) setJobs(data);
        else {
          // Fallback mocks if DB empty
          setJobs([
            { id: 1, title: "Lead AI Solutions Architect", description: "Looking for an expert to build a multi-agent RAG system for enterprise document processing.", platform: "Upwork", budget: "15,000", score: 98, type: "Fixed Price" },
            { id: 2, title: "Senior Full-Stack Engineer (Next.js)", description: "Startup needs help scaling their SaaS platform. Real-time features and high performance required.", platform: "LinkedIn", budget: "120/hr", score: 92, type: "Hourly" },
          ]);
        }
      } catch (e) {
        console.error("Failed to fetch jobs", e);
      }
    };
    fetchJobs();
  }, []);

  const handleStartSwarm = async () => {
    setIsSwarming(true);
    try {
      await fetch('http://localhost:8000/swarm/start', { method: 'POST' });
    } catch (e) {
      console.error("Failed to start swarm", e);
    }
  };

  useEffect(() => {
    const interval = setInterval(() => {
      const messages = [
        "[AGENT] Scanning Upwork for 'AI Engineer'...",
        "[INTEL] Extracted intent from Project #4492: Urgency High.",
        "[STRATEGY] Portfolio match found: 'Aether OS' project.",
        "[PROPOSAL] Generating draft for 'AI Solutions Architect'...",
        "[SCORING] Proposal quality: 94/100."
      ];
      setLogs(prev => [...prev.slice(-9), messages[Math.floor(Math.random() * messages.length)]]);
    }, 3000);
    return () => clearInterval(interval);
  }, []);

  return (
    <main className="container mx-auto px-6 py-10 min-h-screen">
      {/* Header */}
      <header className="flex justify-between items-center mb-12">
        <div>
          <h1 className="text-4xl font-bold tracking-tighter bg-clip-text text-transparent bg-gradient-to-r from-white to-gray-500">
            LUMINA <span className="text-primary">OS</span>
          </h1>
          <p className="text-gray-400 text-sm">Autonomous Freelance Acquisition System v1.0.0</p>
        </div>
        <div className="flex gap-4">
          <div className="flex items-center gap-2 px-4 py-2 glass rounded-full">
            <div className="w-2 h-2 rounded-full bg-green-500 animate-pulse" />
            <span className="text-xs font-mono">AGENTS ACTIVE</span>
          </div>
          <button 
            onClick={handleStartSwarm}
            disabled={isSwarming}
            className={`px-6 py-2 ${isSwarming ? 'bg-gray-700' : 'bg-primary hover:bg-primary/80'} text-white rounded-lg transition-all glow-primary`}
          >
            {isSwarming ? 'Swarm Running...' : 'Start Swarm'}
          </button>
        </div>
      </header>

      <div className="grid grid-cols-12 gap-8">
        {/* Left Col: Opportunity Radar */}
        <div className="col-span-12 lg:col-span-8">
          <div className="flex items-center gap-2 mb-6">
            <Radar className="text-primary animate-spin-slow" size={20} />
            <h2 className="text-xl font-semibold">Opportunity Radar</h2>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {jobs.map((job, i) => (
              <OpportunityCard key={job.id} job={job} index={i} />
            ))}
          </div>
        </div>

        {/* Right Col: Intelligence & Terminal */}
        <div className="col-span-12 lg:col-span-4 space-y-8">
          {/* Stats */}
          <div className="glass-card p-6">
            <h3 className="text-sm font-semibold text-gray-400 uppercase tracking-wider mb-4 flex items-center gap-2">
              <BarChart3 size={16} /> Performance Metrics
            </h3>
            <div className="space-y-4">
              <div>
                <div className="flex justify-between text-xs mb-1">
                  <span>Success Probability</span>
                  <span className="text-primary">84%</span>
                </div>
                <div className="h-1 bg-gray-800 rounded-full overflow-hidden">
                  <motion.div 
                    initial={{ width: 0 }}
                    animate={{ width: "84%" }}
                    className="h-full bg-primary"
                  />
                </div>
              </div>
              <div className="grid grid-cols-2 gap-4">
                <div className="bg-white/5 p-3 rounded-lg border border-white/10">
                  <span className="text-[10px] text-gray-500 block">REPLY RATE</span>
                  <span className="text-xl font-bold">24.8%</span>
                </div>
                <div className="bg-white/5 p-3 rounded-lg border border-white/10">
                  <span className="text-[10px] text-gray-500 block">EST. REVENUE</span>
                  <span className="text-xl font-bold">$12.4k</span>
                </div>
              </div>
            </div>
          </div>

          {/* Terminal */}
          <div className="glass p-4 rounded-xl border border-white/5 h-[300px] flex flex-col">
            <div className="flex items-center gap-2 mb-3 text-xs font-mono text-gray-500">
              <Terminal size={14} /> AGENT_THINKING_LOGS
            </div>
            <div className="flex-1 overflow-y-auto font-mono text-[11px] space-y-2 text-primary/80">
              <AnimatePresence mode="popLayout">
                {logs.map((log, i) => (
                  <motion.div
                    key={i}
                    initial={{ opacity: 0, x: -10 }}
                    animate={{ opacity: 1, x: 0 }}
                    exit={{ opacity: 0, scale: 0.9 }}
                    className="flex gap-2"
                  >
                    <span className="text-gray-600">[{new Date().toLocaleTimeString()}]</span>
                    <span>{log}</span>
                  </motion.div>
                ))}
              </AnimatePresence>
            </div>
          </div>
        </div>
      </div>
    </main>
  );
}
