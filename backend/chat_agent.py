from agents import Agent, ModelSettings

from tools import calculator


normal_agent = Agent(
    name="ChatAgentv1",
    instructions=(
        "You are ChatAgentv1, a helpful assistant. "
        "Answer clearly and concisely."
    ),
    model="gpt-4.1-mini",
)


math_agent = Agent(
    name="ChatAgentv1Math",
    instructions=(
        "You are ChatAgentv1Math. "
        "For math calculations, you must use the calculator tool."
    ),
    tools=[calculator],
    model="gpt-4.1-mini",
    model_settings=ModelSettings(tool_choice="required"),
)