from crewai import Agent
from tools import yt_tool
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = "gpt-3.5-turbo"


## Create a Senior Blog Content Researcher

blog_researcher = Agent(
    role = "Blog Researcher on YouTube Videos",
    goal = "Get the relevant content for the topic {topic} from the YouTube channel",
    verbose = True,
    memory=True,
    backstory=(
        "An expert in understanding videos concerning AI, Data Science, Machine Learning, and Generative AI. The Agent will be provided suggestions as necessary."),
    tools=[yt_tool],
    allow_delegation=True # transferring results to other agent
)


## Creating a Senior Blog Writer Agent with YouTube Tools

blog_writer=Agent(
    role = "Blog Writer",
    goal = "Narrate compelling tech stories about the video {topic}",
    verbose = True,
    memory = True,
    backstory = (
        "With a flair for simplifying complex topics, you craft engaging narratives that captivate and educate, bringing new discoveries to light in an accessible manner."
    ),
    tools = [yt_tool],
    allow_delegations=False
)