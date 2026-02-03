from crewai import Agent
from tools import yt_tool

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

import os 

# Set OpenAI API key from environment variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Define the OpenAI model to be used by the agents
os.environ["OPENAI_MODEL_NAME"] = "gpt-4-0125-preview"

# Agent responsible for researching YouTube videos
blog_researcher = Agent(
    role='Blog Researcher from Youtube Videos',  # Defines the responsibility of the agent
    goal='get the relevant video transcription for the topic {topic} from the provided Yt channel',  # Research objective
    verbose=True,  # Enables detailed logging of agent actions
    memory=True,  # Allows the agent to retain context across steps
    backstory=(
        "Expert in understanding videos in AI Data Science , MAchine Learning And GEN AI and providing suggestion"
    ),  # Domain expertise and behavior guidance
    tools=[yt_tool],  # Tool used to interact with YouTube data
    allow_delegation=True,  # Allows the agent to delegate tasks if needed
)

# Agent responsible for writing blog content
blog_writter = Agent(
    role='Blog Writer',  # Defines the role focused on content creation
    goal='Narrate compelling tech stories about the video {topic} from YT video',  # Writing objective
    verbose=True,  # Enables detailed output during execution
    memory=True,  # Retains context for coherent storytelling
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),  # Writing style and tone definition
    tools=[yt_tool],  # Tool access for referencing video content
    allow_delegation=False,  # Restricts task delegation
)
