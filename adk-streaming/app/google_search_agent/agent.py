from google.adk.agents import Agent
from google.adk.tools import google_search  # Import the tool

# root_agent = Agent(
#    # A unique name for the agent.
#    name="basic_search_agent",
#    # The Large Language Model (LLM) that agent will use.
#    # Please fill in the latest model id that supports live from
#    # https://adk.dev/live/get-started/streaming-python/#supported-models
#    model="gemini-3.5-flash",
#    # A short description of the agent's purpose.
#    description="Agent to answer questions using Google Search.",
#    # Instructions to set the agent's behavior.
#    instruction="You are an expert researcher. You always stick to the facts.",
#    # Add google_search tool to perform grounding with Google search.
#    tools=[google_search]
# )
root_agent = Agent(
    # Change from 'gemini-3.5-flash' to the designated live audio endpoint
    model='gemini-3.8-live', 
    name='root_agent',
    description="Provides a daily breakdown of the latest AI news from around the world.",
    instruction=(
        "You are a helpful voice assistant. Use the 'google_search' tool to retrieve "
        "information when asked, and present it clearly."
    ),
    tools=[google_search],
)
