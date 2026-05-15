import asyncio
from packages.automation.discovery import DiscoveryAgent
from packages.intelligence.analyzer import RequirementAnalyzer
from packages.intelligence.client_scorer import ClientScorer
from apps.api.database import Job, JobAnalysis
from apps.api.db_utils import SessionLocal
import logging

logger = logging.getLogger(__name__)

class IngestionPipeline:
    def __init__(self, openai_api_key: str):
        self.discovery = DiscoveryAgent(headless=True)
        self.analyzer = RequirementAnalyzer(openai_api_key)
        self.scorer = ClientScorer()

    async def run(self, keyword: str):
        logger.info(f"Starting ingestion pipeline for: {keyword}")
        
        # 1. Discover
        raw_jobs = await self.discovery.scan_upwork(keyword)
        
        db = SessionLocal()
        try:
            for raw_job in raw_jobs:
                # Check for duplicates
                existing = db.query(Job).filter(Job.title == raw_job["title"]).first()
                if existing:
                    continue
                
                # 2. Create Job Entry
                job = Job(
                    title=raw_job["title"],
                    description=raw_job["description"],
                    platform=raw_job["platform"],
                    budget=raw_job["budget"],
                    status="discovered"
                )
                db.add(job)
                db.commit()
                db.refresh(job)
                
                # 3. Analyze (Background)
                analysis_data = await self.analyzer.analyze(job.description)
                
                # 4. Score
                toxicity = self.scorer.detect_toxicity(job.description)
                
                # 5. Save Analysis
                analysis = JobAnalysis(
                    job_id=job.id,
                    urgency=analysis_data["urgency"],
                    complexity=analysis_data["technical_complexity"],
                    required_skills=", ".join(analysis_data["required_skills"]),
                    red_flags=", ".join(analysis_data["red_flags"]),
                    profitability_score=85.0 # Placeholder calculation
                )
                db.add(analysis)
                
                # Update job status
                job.status = "analyzed"
                job.match_score = 90.0 # Placeholder
                
                db.commit()
                logger.info(f"Ingested and analyzed: {job.title}")
                
        except Exception as e:
            logger.error(f"Pipeline error: {e}")
        finally:
            db.close()

if __name__ == "__main__":
    # Example trigger
    pipeline = IngestionPipeline("sk-...")
    # asyncio.run(pipeline.run("AI Engineer"))
    pass
