import os
import dotenv
from crewai import Crew, Agent, Task, LLM
from crewai.project import CrewBase, agent, task, crew
from crewai.project import CrewBase, agent, task, crew
from tools import search_tool, scrape_tool

dotenv.load_dotenv()

@CrewBase
class NewsReaderCrew:
    """News Reader Crew"""
    agents_config = "config/news_agents.yaml"
    tasks_config = "config/news_tasks.yaml"

    def __init__(self):
        self.llm = LLM(
            model="gemini/gemini-2.0-flash",
            api_key=os.environ["GEMINI_API_KEY"]
        )

    @agent
    def news_hunter_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["news_hunter_agent"],
            tools=[search_tool, scrape_tool],
            llm=self.llm,
            verbose=True
        )

    @agent
    def summarizer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["summarizer_agent"],
            tools=[scrape_tool],
            llm=self.llm,
            verbose=True
        )

    @agent
    def curator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["curator_agent"],
            llm=self.llm,
            verbose=True
        )

    @task
    def content_harvesting_task(self) -> Task:
        return Task(
            config=self.tasks_config["content_harvesting_task"],
        )

    @task
    def summarization_task(self) -> Task:
        return Task(
            config=self.tasks_config["summarization_task"],
        )

    @task
    def final_report_assembly_task(self) -> Task:
        return Task(
            config=self.tasks_config["final_report_assembly_task"],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
        )

def main():
    result = NewsReaderCrew().crew().kickoff(
        inputs={
            "topic": "near protocol news",
        }
    )

    for task_output in result.tasks_output:
        print(task_output)

if __name__ == "__main__":
    main()
