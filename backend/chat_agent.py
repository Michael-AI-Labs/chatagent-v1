from agents import Agent, ModelSettings

from tools import (
    calculator,
    current_time,
    unit_converter,
)


normal_agent = Agent(
    name="ChatAgentv1",
    instructions=(
        "You are ChatAgentv1, a helpful assistant."
    ),
    model="gpt-4.1-mini",
)


math_agent = Agent(
    name="MathAgent",
    instructions=(
        "You must use the calculator tool for math."
    ),
    tools=[calculator],
    model="gpt-4.1-mini",
    model_settings=ModelSettings(tool_choice="required"),
)


time_agent = Agent(
    name="TimeAgent",
    instructions=(
        "Use the current_time tool when asked about time/date."
    ),
    tools=[current_time],
    model="gpt-4.1-mini",
    model_settings=ModelSettings(tool_choice="required"),
)


conversion_agent = Agent(
    name="ConversionAgent",
    instructions=(
        "Use the unit_converter tool for unit conversions."
    ),
    tools=[unit_converter],
    model="gpt-4.1-mini",
    model_settings=ModelSettings(tool_choice="required"),
)