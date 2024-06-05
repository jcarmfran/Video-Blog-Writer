from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

## Research Task

research_task= Task(
    description = ("identify the video {topic}."
                   "Get detailed information about the video from the channel."),
    expected_output="A comprehensive 3 paragraph long report based on the {topic} of the video channel",
    tools = [yt_tool],
    agent= blog_researcher
)



writing_task= Task(
    description = "Get the information from the YouTube channel on the topic {topic}.",
    expected_output="Summarize the info from the YouTube channel video on the topic {topic} and create the content for the blog.",
    tools = [yt_tool],
    agent = blog_writer,
    async_execution=False,
    output_file="new-blog-post.md"
)