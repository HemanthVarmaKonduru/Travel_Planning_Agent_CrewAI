from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from travelagent.tools.custom_tool import FlightSearchTool, HotelSearchTool, ActivitySearchTool, GeneralSearchTool
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Travelplanneragent():
    """Travelplanneragent crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def clarifier_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['clarifier_agent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def flight_research_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['flight_research_agent'], # type: ignore[index]
            tools=[FlightSearchTool(), GeneralSearchTool()],
            verbose=True
        )

    @agent
    def stay_research_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['stay_research_agent'], # type: ignore[index]
            tools=[HotelSearchTool(), GeneralSearchTool()],
            verbose=True
        )

    @agent
    def activity_planner_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['activity_planner_agent'], # type: ignore[index]
            tools=[ActivitySearchTool(), GeneralSearchTool()],
            verbose=True
        )

    @agent
    def logistics_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['logistics_agent'], # type: ignore[index]
            tools=[GeneralSearchTool()],
            verbose=True
        )

    @agent
    def budget_estimator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['budget_estimator_agent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def synthesis_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['synthesis_agent'], # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def clarify_trip_requirements(self) -> Task:
        return Task(
            config=self.tasks_config['clarify_trip_requirements'], # type: ignore[index]
        )

    @task
    def research_flights(self) -> Task:
        return Task(
            config=self.tasks_config['research_flights'], # type: ignore[index]
        )

    @task
    def research_accommodations(self) -> Task:
        return Task(
            config=self.tasks_config['research_accommodations'], # type: ignore[index]
        )

    @task
    def plan_daily_activities(self) -> Task:
        return Task(
            config=self.tasks_config['plan_daily_activities'], # type: ignore[index]
        )

    @task
    def coordinate_logistics(self) -> Task:
        return Task(
            config=self.tasks_config['coordinate_logistics'], # type: ignore[index]
        )

    @task
    def estimate_total_budget(self) -> Task:
        return Task(
            config=self.tasks_config['estimate_total_budget'], # type: ignore[index]
        )

    @task
    def compile_final_itinerary(self) -> Task:
        return Task(
            config=self.tasks_config['compile_final_itinerary'], # type: ignore[index]
            output_file='travel_itinerary.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Travelplanneragent crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
