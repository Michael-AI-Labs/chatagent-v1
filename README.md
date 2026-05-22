# ChatAgent Project

Simple chat app with a Streamlit frontend, FastAPI backend, and OpenAI Agents SDK routing.

## Requirements

- Python 3.13+
- `uv`

## Setup

Install dependencies:

```bash
uv sync
```

## Run The App

Start the FastAPI backend:

```bash
cd backend
uv run python main.py
```

Start the Streamlit frontend from the project root in a second terminal:

```bash
uv run streamlit run frontend/streamlit_app.py
```

## Run Tests

Run the classifier tests from the project root:

```bash
uv run python -m unittest tests.test_chat -v
```

## Notes

- Search requests are routed to `SearchAgent`.
- Time-sensitive questions depend on your OpenAI API configuration and network access.
