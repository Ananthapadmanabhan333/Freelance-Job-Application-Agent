from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from apps.api.database import Job, JobAnalysis
from apps.api.db_utils import SessionLocal, init_db
from packages.intelligence.ingestion import IngestionPipeline
import os

app = FastAPI(title="Lumina AI API", version="1.0.0")

# Initialize DB on startup
@app.on_event("startup")
def startup_event():
    init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Lumina Autonomous Freelance OS API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/jobs")
async def get_jobs():
    db = SessionLocal()
    jobs = db.query(Job).all()
    db.close()
    return jobs

@app.post("/swarm/start")
async def start_swarm(keyword: str = "AI Agent"):
    pipeline = IngestionPipeline(os.getenv("OPENAI_API_KEY"))
    # In a real app, this would be a background task
    asyncio.create_task(pipeline.run(keyword))
    return {"message": f"Swarm started for {keyword}"}

@app.websocket("/ws/agents")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Agent Log: {data}")
    except WebSocketDisconnect:
        logger.info("Client disconnected from WebSocket")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
