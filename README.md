# Lumina: Autonomous Freelance OS

Lumina is a world-class, production-grade autonomous system for freelance acquisition. It functions as a "Devin-style" workflow engine that handles everything from discovery to proposal generation and communication.

## 🚀 Key Features
- **Autonomous Discovery Swarm**: Multi-platform browser agents scanning Upwork, LinkedIn, etc.
- **Deep Intent Analysis**: AI-powered extraction of technical requirements, urgency, and budget realism.
- **Hyper-Personalized Proposals**: Synthesizes your portfolio with client needs for maximum conversion.
- **Cinematic Dashboard**: A futuristic, real-time command center for managing your freelance business.
- **Multi-Agent Orchestration**: LangGraph-powered workflow managing the entire sales pipeline.

## 🛠 Tech Stack
- **Frontend**: Next.js 15, Tailwind CSS, Framer Motion, Recharts.
- **Backend**: FastAPI, LangGraph, OpenAI GPT-4o.
- **Automation**: Playwright + Stealth.
- **Database**: PostgreSQL, Redis, Qdrant/Pinecone.

## 📦 Project Structure
- `apps/web`: Next.js 15 frontend application.
- `apps/api`: FastAPI backend and orchestration engine.
- `packages/agents`: Core LangGraph orchestrator and agent definitions.
- `packages/automation`: Browser automation (Playwright) scripts.
- `packages/intelligence`: NLP and scoring engines.

## 🚦 Getting Started

### 1. Setup Environment
```bash
cp .env.example .env
# Fill in your OPENAI_API_KEY and DATABASE_URL
```

### 2. Install Dependencies
```bash
# Frontend
cd apps/web && npm install

# Backend
cd apps/api && pip install -r requirements.txt
```

### 3. Run the System
```bash
# Start Backend
cd apps/api && uvicorn main:app --reload

# Start Frontend
cd apps/web && npm run dev
```

## 🛡 Security & Ethics
Lumina uses advanced stealth browsing to avoid detection but should be used responsibly. Always review AI-generated proposals before sending to maintain professional integrity.

---
Built with ⚡ by the Lumina AI Team.
