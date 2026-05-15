from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI

class LuminaCrew:
    def __init__(self, api_key: str):
        self.llm = ChatOpenAI(model="gpt-4o", openai_api_key=api_key)

    def run(self, job_description: str, portfolio: str):
        # 1. Define Agents
        researcher = Agent(
            role='Market Intelligence Analyst',
            goal='Analyze job descriptions for hidden requirements and client intent',
            backstory='Expert in reading between the lines of freelance job posts.',
            llm=self.llm,
            verbose=True
        )

        writer = Agent(
            role='Senior Proposal Strategist',
            goal='Craft hyper-personalized, high-conversion proposals',
            backstory='Award-winning copywriter specializing in technical sales pitches.',
            llm=self.llm,
            verbose=True
        )

        # 2. Define Tasks
        analysis_task = Task(
            description=f'Analyze this job: {job_description}',
            agent=researcher,
            expected_output='A detailed report on job requirements and client expectations.'
        )

        proposal_task = Task(
            description=f'Write a proposal using this portfolio: {portfolio}',
            agent=writer,
            expected_output='A finished, persuasive proposal ready to be sent.'
        )

        # 3. Form the Crew
        crew = Crew(
            agents=[researcher, writer],
            tasks=[analysis_task, proposal_task],
            process=Process.sequential
        )

        return crew.kickoff()
