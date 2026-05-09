from agents import Agent


chat_agent = Agent(
    name="ChatAgentv1",
    instructions=(
        "You are ChatAgentv1, a helpful assistant. "
        "Give clear, concise answers."
    ),
    model="gpt-4.1-mini",
)