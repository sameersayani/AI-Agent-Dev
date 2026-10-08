# AI Agent Dev

This repository contains a small set of Google ADK-based agent demos for experimenting with AI assistants, news summaries, and web-grounded search.

## Project overview

- `news_agent/` - A simple news assistant that exposes a custom tool returning AI-related headlines.
- `adk-streaming/app/google_search_agent/` - A streaming/search-enabled agent using Google Search grounding.
- `venv/` - Local Python environment for the project.

## Prerequisites

- Python 3.10+
- A Google API key with access to Gemini/Google AI APIs
- Google ADK installed in the project environment

## Environment setup

Create or update the `.env` files with your Google credentials:

```env
GOOGLE_GENAI_USE_ENTERPRISE=0
GOOGLE_API_KEY=your_google_api_key_here
```

For this project, the following files are used:

- `news_agent/.env`
- `adk-streaming/.env`

## Local setup

```powershell
cd "D:\My Projects\AI-Agent-Dev"
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install google-adk python-dotenv certifi
```

If you see certificate issues in the local environment, run:

```powershell
$env:SSL_CERT_FILE = "$(python -m certifi)"
```

## Run the agents

### 1) News agent

From the project root:

```powershell
cd "D:\My Projects\AI-Agent-Dev"
adk web news_agent --no-avatar
```

### 2) Streaming / search agent

From the `adk-streaming` folder:

```powershell
cd "D:\My Projects\AI-Agent-Dev\adk-streaming"
adk web app --no-avatar
```

You can also run the app with the default reload behavior:

```powershell
adk web --no-reload
```

## Notes

- The news agent is a lightweight demo that returns structured AI news data from a custom tool.
- The search agent demonstrates Google Search grounding and is intended for interactive experimentation.
- The project is best used as a learning sandbox for building and testing ADK-powered agents.
