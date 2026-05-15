from sqlalchemy import create_all, Column, Integer, String, Text, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import datetime

Base = declarative_base()

class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    external_id = Column(String, unique=True, index=True)
    platform = Column(String)
    title = Column(String)
    description = Column(Text)
    budget = Column(String)
    posted_at = Column(DateTime, default=datetime.datetime.utcnow)
    match_score = Column(Float)
    status = Column(String, default="discovered") # discovered, analyzed, ignored, applied
    
    analysis = relationship("JobAnalysis", back_populates="job", uselist=False)
    proposals = relationship("Proposal", back_populates="job")

class JobAnalysis(Base):
    __tablename__ = "job_analyses"
    id = Column(Integer, primary_key=True)
    job_id = Column(Integer, ForeignKey("jobs.id"))
    urgency = Column(String)
    complexity = Column(Integer)
    required_skills = Column(Text)
    red_flags = Column(Text)
    profitability_score = Column(Float)
    
    job = relationship("Job", back_populates="analysis")

class Proposal(Base):
    __tablename__ = "proposals"
    id = Column(Integer, primary_key=True)
    job_id = Column(Integer, ForeignKey("jobs.id"))
    content = Column(Text)
    status = Column(String, default="draft") # draft, sent, replied, won, lost
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    job = relationship("Job", back_populates="proposals")

class PortfolioProject(Base):
    __tablename__ = "portfolio_projects"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    tech_stack = Column(Text)
    url = Column(String)
    embedding_id = Column(String) # For vector search
