import os
from crewai import LLM, Agent, Task, Crew
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")


llm = LLM(model="gpt-4", temperature=0.7, max_tokens=500)

search_tool = SerperDevTool()


researcher = Agent(
    llm=llm,
    role="Senior AI Researcher",
    goal="Identify recent advancements in AI for medical applications.",
    backstory="An experienced AI researcher focusing on healthcare innovations.",
    allow_delegation=False,
    tools=[search_tool],
    verbose=1,
)

search_task = Task(
    description="Research recent advancements in AI for medical imaging.",
    expected_output="A brief summary of recent technologies and their potential impact on medical diagnostics.",
    output_file="research_output.txt",
    agent=researcher,
)


blogger = Agent(
    llm=llm,
    role="AI Blogger",
    goal="Write a blog post about the latest advancements in AI for medical imaging.",
    backstory="An experienced AI blogger with a passion for healthcare innovation.",
    allow_delegation=False,
    verbose=1,
)

blog_task = Task(
    description="Write a blog post about the latest advancements in AI for medical imaging.",
    expected_output="A well-researched blog post highlighting the recent technologies and their potential impact on medical diagnostics.",
    output_file="blog_output.txt",
    agent=blogger,
    input_file="research_output.txt",
)

crew = Crew(agents=[researcher, blogger], tasks=[search_task, blog_task], verbose=1)
result = crew.kickoff()
print("Task Result:", result)
