from agents import Runner

from chat_agent import (
    normal_agent,
    math_agent,
    time_agent,
    conversion_agent,
)


def classify_request(message: str) -> str:
    message = message.lower()

    math_keywords = [
        "calculate",
        "plus",
        "minus",
        "*",
        "/",
        "+",
        "=",
    ]

    time_keywords = [
        "time",
        "date",
        "day",
        "clock",
    ]

    conversion_keywords = [
        "convert",
        "kilometers",
        "miles",
        "pounds",
        "kilograms",
    ]

    if any(keyword in message for keyword in math_keywords):
        return "math"

    if any(keyword in message for keyword in time_keywords):
        return "time"

    if any(keyword in message for keyword in conversion_keywords):
        return "conversion"

    return "normal"


async def handle_chat(message, messages):
    classification = classify_request(message)

    if classification == "math":
        selected_agent = math_agent

    elif classification == "time":
        selected_agent = time_agent

    elif classification == "conversion":
        selected_agent = conversion_agent

    else:
        selected_agent = normal_agent

    conversation_history = []

    for msg in messages:
        if hasattr(msg, "role") and hasattr(msg, "content"):
            role = msg.role
            content = msg.content
        else:
            role = msg["role"]
            content = msg["content"]

        conversation_history.append(
            {
                "role": role,
                "content": content,
            }
        )

    if not conversation_history or conversation_history[-1]["content"] != message:
        conversation_history.append(
            {
                "role": "user",
                "content": message,
            }
        )

    result = await Runner.run(
        selected_agent,
        conversation_history,
    )

    return result.final_output
