from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

@CrewBase
class LegalDocReview():
    """LegalDocReview crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def clause_extractor(self) -> Agent:
        return Agent(
            config=self.agents_config['clause_extractor'],
            verbose=True
        )

    @agent
    def risk_detector(self) -> Agent:
        return Agent(
            config=self.agents_config['risk_detector'],
            verbose=True
        )

    @agent
    def summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config['summarizer'],
            verbose=True
        )

    # @task
    # def extract_clauses_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['extract_clauses_task'],
    #     )

    # @task
    # def detect_risks_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['detect_risks_task'],
    #     )

    # @task
    # def summarize_document_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['summarize_document_task'],
    #          output_file='outputs/report.md'
    #     )

    @task
    def extract_clauses_task(self) -> Task:
        return Task(
            config=self.tasks_config['extract_clauses_task'],
            output_file='outputs/clauses_output.md'  # ✅ Save clause extraction
        )

    @task
    def detect_risks_task(self) -> Task:
        return Task(
            config=self.tasks_config['detect_risks_task'],
            output_file='outputs/risk_report.md'  # ✅ Save risk detection
        )

    @task
    def summarize_document_task(self) -> Task:
        return Task(
            config=self.tasks_config['summarize_document_task'],
            output_file='outputs/final_summary.md'  # ✅ Save final summary
        )

    @crew
    def crew(self) -> Crew:
        """Creates the LegalDocReview crew"""
        return Crew(
            agents=self.agents,  # Created by decorators
            tasks=self.tasks,    # Created by decorators
            process=Process.sequential,
            verbose=True,
        )


