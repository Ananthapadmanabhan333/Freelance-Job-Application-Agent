from typing import Dict, List
import json
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

class JobAnalysis(BaseModel):
    intent: str = Field(description="The primary goal of the project")
    urgency: str = Field(description="Low, Medium, or High")
    technical_complexity: int = Field(description="Score from 1-10")
    required_skills: List[str] = Field(description="List of core technical skills")
    client_style: str = Field(description="Professional, Casual, or Technical")
    red_flags: List[str] = Field(description="Potential issues or scam indicators")
    estimated_budget_fairness: str = Field(description="Underpaid, Fair, or Generous")

class RequirementAnalyzer:
    def __init__(self, api_key: str):
        self.llm = ChatOpenAI(model="gpt-4o", openai_api_key=api_key)
        self.parser = JobAnalysis

    async def analyze(self, job_description: str) -> Dict:
        prompt = ChatPromptTemplate.from_template("""
        You are a senior technical recruiter and business analyst. 
        Analyze the following freelance job description and extract deep insights.
        
        JOB DESCRIPTION:
        {description}
        
        Provide a structured analysis including intent, urgency, technical complexity, skills, client style, red flags, and budget fairness.
        """)
        
        chain = prompt | self.llm.with_structured_output(self.parser)
        result = await chain.ainvoke({"description": job_description})
        return result.dict()

if __name__ == "__main__":
    # Example usage
    import asyncio
    analyzer = RequirementAnalyzer(api_key="your-api-key")
    # asyncio.run(analyzer.analyze("Looking for a developer to build a bot..."))
    pass
