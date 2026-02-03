from crewai_tools import YoutubeChannelSearchTool

# Initialize a tool to search and extract data from a specific YouTube channel
yt_tool = YoutubeChannelSearchTool(
    youtube_channel_handle="https://www.youtube.com/@IBMTechnology"  # Target YouTube channel for content retrieval
)
