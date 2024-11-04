from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import CSVSearchTool, FileReadTool

@CrewBase
class TalentConnectionCrew:
    """Talent Connection crew for matching a single candidate with relevant opportunities."""
    
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    @agent
    def csv_reader(self) -> Agent:
        """Agent dedicated to reading and structuring data from CSV files."""
        return Agent(
            config=self.agents_config['csv_reader'],
            tools=[FileReadTool(), CSVSearchTool()],
            allow_delegation=False,
            verbose=True
        )
    
    @agent
    def talent_researcher(self) -> Agent:
        """Agent that processes a single candidate profile to find suitable matches."""
        return Agent(
            config=self.agents_config['talent_researcher'],
            allow_delegation=False,
            verbose=True
        )
        
    @agent
    def opportunity_hunter(self) -> Agent:
        """Agent that searches for and summarizes relevant opportunities."""
        return Agent(
            config=self.agents_config['opportunity_hunter'],
            allow_delegation=False,
            verbose=True
        )
        
    @task
    def read_opportunities_task(self) -> Task:
        """Task for CSV Reader to load opportunities data from the CSV file."""
        return Task(
            config=self.tasks_config['read_opportunities_task'],
            agent=self.csv_reader()
        )
        
    @task
    def find_talent_matches_task(self) -> Task:
        """Task for Talent Researcher to find opportunities matching the candidate’s profile."""
        return Task(
            config=self.tasks_config['find_talent_matches_task'],
            agent=self.talent_researcher(),
            context=[self.read_opportunities_task()]
        )
        
    @task
    def find_opportunities_task(self) -> Task:
        """Task for Opportunity Hunter to further refine and organize the best opportunities."""
        return Task(
            config=self.tasks_config['find_opportunities_task'],
            agent=self.opportunity_hunter(),
            context=[self.find_talent_matches_task()]
        )
        
    @task
    def summarize_candidate_profile_task(self) -> Task:
        """Task for Talent Researcher to summarize the candidate’s profile."""
        return Task(
            config=self.tasks_config['summarize_candidate_profile_task'],
            agent=self.talent_researcher(),
            context=[self.find_talent_matches_task()]
        )
        
    @task 
    def summarize_opportunities_task(self) -> Task:
        """Task for Opportunity Hunter to summarize the identified opportunities."""
        return Task(
            config=self.tasks_config['summarize_opportunities_task'],
            agent=self.opportunity_hunter(),
            context=[self.find_opportunities_task()],
            output_file='outputs/opportunities_summary.txt'
        )
        
    @crew
    def crew(self) -> Crew:
        """Creates the Talent Connection crew."""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
