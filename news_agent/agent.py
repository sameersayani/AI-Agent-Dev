import json
from google.adk.agents.llm_agent import Agent

# Tool implementation to fetch AI news
def get_latest_ai_news() -> dict:
    """Fetches the latest artificial intelligence news, providing one major headline for each recent day."""
    # In a production environment, this would call a real news API or web scraper.
    # The return format is a JSON-compatible dictionary structured by date.
    news_data = {
        "status": "success",
        "articles": [
            {
                "date": "2026-10-08",
                "headline": "OpenAI releases next-generation reasoning model with advanced coding proficiency.",
                "source": "TechCrunch"
            },
            {
                "date": "2026-10-07",
                "headline": "Google DeepMind unveils localized weather forecasting AI operating at 10x efficiency.",
                "source": "Nature"
            },
            {
                "date": "2026-10-06",
                "headline": "Anthropic signs historic compute partnership to expand Claude infrastructure.",
                "source": "Reuters"
            }
        ]
    }
    return news_data

root_agent = Agent(
    model='gemini-3.5-flash',  # Updated to framework default
    name='root_agent',
    description="Provides a daily breakdown of the latest AI news from around the world.",
    instruction=(
        "You are a tech journalist assistant. Use the 'get_latest_ai_news' tool to retrieve "
        "the latest AI developments. Always format your final response strictly as a raw JSON string "
        "containing the dates and their respective news headlines."
    ),
    tools=[get_latest_ai_news],
)
