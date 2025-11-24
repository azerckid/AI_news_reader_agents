import os
import dotenv
from crewai import Crew, Agent, Task, LLM
from crewai.project import CrewBase, agent, task, crew
from tools import count_letters

dotenv.load_dotenv()

@CrewBase
class TranslatorCrew:
    """Translator Crew"""
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    def __init__(self):
        self.llm = LLM(
            model="gemini/gemini-2.5-flash-preview-09-2025",
            api_key=os.environ["GEMINI_API_KEY"]
        )

    @agent
    def translator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["translator_agent"],
            llm=self.llm,
            verbose=True
        )

    @agent
    def counter_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["counter_agent"],
            tools=[count_letters],
            llm=self.llm,
            verbose=True
        )

    @task
    def translate_task(self) -> Task:
        return Task(
            config=self.tasks_config["translate_task"],
        )

    @task
    def retranslate_task(self) -> Task:
        return Task(
            config=self.tasks_config["retranslate_task"],
        )

    @task
    def count_task(self) -> Task:
        return Task(
            config=self.tasks_config["count_task"],
        )

    @crew
    def assemble_crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
        )

def main():
    TranslatorCrew().assemble_crew().kickoff(
        inputs={
            "sentence": "I'm Henry and I like to ride my bicicle in Napoli",
        }
    )

if __name__ == "__main__":
    main()
