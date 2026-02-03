from crewai import Crew, Process
from agents import blog_researcher, blog_writter
from tasks import research_task, write_task

# Create a crew by grouping agents and assigning tasks
crew = Crew(
    agents=[blog_researcher, blog_writter],  # Agents participating in the workflow
    tasks=[research_task, write_task],  # Tasks executed by the crew
    process=Process.sequential,  # Ensures tasks run one after another in order
    memory=True,  # Enables shared memory across agents and tasks
    cache=True,  # Caches intermediate results to improve efficiency
    max_rpm=100,  # Limits the maximum requests per minute
    share_crew=True  # Allows agents to share context and outputs
)

# Trigger the crew execution with the provided topic as input
result = crew.kickoff(
    inputs={'topic': "Generative vs Agentic AI: Shaping the Future of AI Collaboration"}
)

# Output the final result produced by the crew
print(result)
