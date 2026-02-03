from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writter

# Task responsible for researching the YouTube video content
research_task = Task(
    description=(
        "Identify the video {topic}."
        "Get detailed information about the video from the channel video."
    ),  # Defines what information needs to be gathered
    expected_output='A comprehensive 4 paragraphs long report based on the {topic} of video content.',  # Expected research deliverable
    tools=[yt_tool],  # Tool used to fetch and analyze YouTube data
    agent=blog_researcher  # Agent assigned to perform the research
)

# Task responsible for writing the blog content
write_task = Task(
    description=("get the info from the youtube channel on the topic {topic}."),  # Writing task instructions
    expected_output='Summarize the info from the youtube channel video on the topic{topic} and create the content for the blog',  # Final content requirement
    tools=[yt_tool],  # Tool used to reference YouTube content
    agent=blog_writter,  # Agent assigned to write the blog
    async_execution=False,  # Ensures the task runs synchronously
    output_file='blog-post.md'  # Stores the generated blog content in a markdown file
)
