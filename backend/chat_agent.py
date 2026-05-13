from agents import Agent

from tools import calculator


chat_agent = Agent(
    name="ChatAgentv1",
    instructions=(
        "You are ChatAgentv1, a helpful assistant. "
        "Use the calculator tool for math calculations."
    ),
    tools=[calculator],
    model="gpt-4.1-mini",
)