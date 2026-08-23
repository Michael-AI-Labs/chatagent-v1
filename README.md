# ChatAgent v1

An AI chat application with routing, session memory, tool use, and web search.

Built as part of **Michael AI Labs**, this project explores how a small AI assistant can route different types of requests to specialized behaviors while maintaining a simple FastAPI backend and Streamlit interface.

## What It Does

ChatAgent v1 accepts natural-language requests and routes them based on the type of task.

The application can:

- handle general chat
- maintain session-level conversation memory
- perform calculations
- convert units
- answer time-related questions
- route search-oriented questions to web search
- return responses through a Streamlit chat interface

## Core Features

- **Request Routing** — classifies incoming prompts and directs them to the appropriate behavior
- **Session Memory** — maintains conversational context within a user session
- **Tool Use** — supports calculator, time, and unit-conversion tools
- **Web Search** — routes search-oriented requests to a dedicated search path
- **FastAPI Backend** — exposes the chat service through an API layer
- **Streamlit Frontend** — provides a lightweight conversational interface

## Tech Stack

- **Python 3.13+**
- **FastAPI** — backend API
- **Streamlit** — local chat interface
- **OpenAI Agents SDK** — agent orchestration and tool use
- **OpenAI API** — model responses
- **uv** — environment and dependency management
- **unittest** — automated testing

## Project Structure

```text
chatagent-v1/
├── backend/
├── frontend/
│   └── streamlit_app.py
├── tests/
├── .python-version
├── pyproject.toml
├── uv.lock
└── README.md
```

## Running Locally

Install the project dependencies with `uv`.

```bash
uv sync
```

### Start the FastAPI Backend

From the project:

```bash
cd backend
uv run python main.py
```

### Start the Streamlit Frontend

Open a second terminal from the project root:

```bash
uv run streamlit run frontend/streamlit_app.py
```

## Environment Variables

The application requires an OpenAI API key.

Keep API credentials in your local environment and **do not commit them to GitHub**.

For example:

```text
OPENAI_API_KEY=your_api_key_here
```

Local `.env` files are excluded through `.gitignore`.

## Example Capabilities

Example requests include:

```text
What time is it in Tokyo?
```

```text
Convert 5 miles to kilometers.
```

```text
What is 18 percent of 245?
```

```text
Search for the latest information about a current topic.
```

The application routes each request according to the type of task.

## Testing

Run the classifier and chat tests from the project root:

```bash
uv run python -m unittest tests.test_chat -v
```

## Project Goals

This project demonstrates several practical AI application patterns:

- separating a conversational AI application into frontend and backend layers
- routing user requests to specialized agent behaviors
- integrating tools into an AI assistant
- maintaining lightweight session memory
- using web search for time-sensitive or external information
- testing routing behavior and API responses
- building a small multi-capability agent as a portfolio project

## Status

**Completed portfolio project**

ChatAgent v1 is functional, tested, and documented. It served as an early practical exploration of routing, tools, memory, and web search in an AI application.

## Michael AI Labs

ChatAgent v1 is part of **Michael AI Labs**, a collection of practical AI application experiments and portfolio projects.
