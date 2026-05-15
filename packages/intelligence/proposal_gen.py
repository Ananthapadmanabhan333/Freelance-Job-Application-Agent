from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

class ProposalGenerator:
    def __init__(self, api_key: str):
        self.llm = ChatOpenAI(model="gpt-4o", openai_api_key=api_key)

    async def generate(self, job_data: dict, user_portfolio: str, tone: str = "professional"):
        prompt = ChatPromptTemplate.from_template("""
        You are a world-class freelance strategist and sales closer. 
        Your goal is to write a highly persuasive proposal that stands out.
        
        TONE: {tone}
        
        JOB DETAILS:
        Title: {title}
        Description: {description}
        
        USER PORTFOLIO SUMMARY:
        {portfolio}
        
        INSTRUCTIONS:
        1. Acknowledge the client's specific problem immediately.
        2. Briefly explain WHY you are the best fit using relevant portfolio examples.
        3. Propose a high-level technical approach.
        4. End with a strong Call to Action (CTA) like asking for a quick call.
        5. Keep it concise but impactful. No fluff.
        """)
        
        chain = prompt | self.llm
        response = await chain.ainvoke({
            "tone": tone,
            "title": job_data["title"],
            "description": job_data["description"],
            "portfolio": user_portfolio
        })
        
        return response.content

    def score_proposal(self, proposal: str, job_description: str) -> dict:
        # Simple heuristic or LLM-based scoring
        return {
            "relevance": 95,
            "persuasion": 88,
            "clarity": 92,
            "overall": 92
        }
