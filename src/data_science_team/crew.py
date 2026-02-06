from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from data_science_team.tools.custom_tool import IrisDataFetcher, StatsSummaryTool, ModelPersistenceTool

@CrewBase
class DataScienceTeam():
    """DataScienceTeam crew for Iris Classification Demo"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # --- Leadership Agents ---
    @agent
    def chief_data_officer(self) -> Agent:
        return Agent(config=self.agents_config['chief_data_officer'], verbose=True)

    @agent
    def data_science_manager(self) -> Agent:
        return Agent(config=self.agents_config['data_science_manager'], verbose=True)

    @agent
    def product_manager(self) -> Agent:
        return Agent(config=self.agents_config['product_manager'], verbose=True)

    # --- Core Technical Agents ---
    @agent
    def data_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['data_engineer'],
            tools=[IrisDataFetcher()],
            verbose=True
        )

    @agent
    def data_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['data_analyst'],
            tools=[StatsSummaryTool()],
            verbose=True
        )

    @agent
    def data_scientist(self) -> Agent:
        return Agent(config=self.agents_config['data_scientist'], verbose=True)

    @agent
    def ml_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['ml_engineer'],
            tools=[ModelPersistenceTool()],
            verbose=True
        )

    # --- Specialized Support Agents ---
    @agent
    def data_architect(self) -> Agent:
        return Agent(config=self.agents_config['data_architect'], verbose=True)

    @agent
    def business_analyst(self) -> Agent:
        return Agent(config=self.agents_config['business_analyst'], verbose=True)

    @agent
    def mlops_engineer(self) -> Agent:
        return Agent(config=self.agents_config['mlops_engineer'], verbose=True)

    @agent
    def ai_ethicist(self) -> Agent:
        return Agent(config=self.agents_config['ai_ethicist'], verbose=True)

    @agent
    def frontend_engineer(self) -> Agent:
        return Agent(config=self.agents_config['frontend_engineer'], verbose=True)

    # --- Tasks ---
    # These map directly to the keys in your tasks.yaml
    @task
    def strategic_alignment_task(self) -> Task:
        return Task(config=self.tasks_config['strategic_alignment_task'])

    @task
    def product_roadmap_task(self) -> Task:
        return Task(config=self.tasks_config['product_roadmap_task'])

    @task
    def data_architecture_task(self) -> Task:
        return Task(config=self.tasks_config['data_architecture_task'])

    @task
    def data_engineering_task(self) -> Task:
        return Task(config=self.tasks_config['data_engineering_task'])

    @task
    def exploratory_analysis_task(self) -> Task:
        return Task(config=self.tasks_config['exploratory_analysis_task'])

    @task
    def business_requirements_task(self) -> Task:
        return Task(config=self.tasks_config['business_requirements_task'])

    @task
    def model_training_task(self) -> Task:
        return Task(config=self.tasks_config['model_training_task'])

    @task
    def model_deployment_preparation_task(self) -> Task:
        return Task(config=self.tasks_config['model_deployment_preparation_task'])

    @task
    def mlops_monitoring_task(self) -> Task:
        return Task(config=self.tasks_config['mlops_monitoring_task'])

    @task
    def frontend_demo_task(self) -> Task:
        return Task(config=self.tasks_config['frontend_demo_task'])

    @task
    def ethical_review_task(self) -> Task:
        return Task(config=self.tasks_config['ethical_review_task'])

    @task
    def project_management_review_task(self) -> Task:
        return Task(config=self.tasks_config['project_management_review_task'])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential, # Ensures the "paper trail" flows correctly
            verbose=True
        )