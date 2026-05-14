from agents import Runner

from chat_agent import normal_agent, math_agent
from schemas import ChatMessage


def _build_conversation_input(message: str, messages: list[ChatMessage]) -> str:
    history_lines: list[str] = []

    for item in messages[:-1]:
        role = "User" if item.role == "user" else "Assistant"
        history_lines.append(f"{role}: {item.content}")

    history_text = "\n".join(history_lines) if history_lines else "No previous conversation."

    return (
        "Use the conversation history below to answer consistently and remember prior context.\n\n"
        f"Conversation history:\n{history_text}\n\n"
        f"Latest user message:\nUser: {message}"
    )


def is_math_request(message: str) -> bool:
    math_keywords = [
        "calculate",
        "what is",
        "plus",
        "minus",
        "multiplied",
        "divided",
        "+",
        "-",
        "*",
        "/",
        "=",
    ]

    return any(keyword in message.lower() for keyword in math_keywords)


async def handle_chat(message: str, messages: list[ChatMessage]) -> str:
    selected_agent = math_agent if is_math_request(message) else normal_agent
    runner_input = _build_conversation_input(message, messages)

    result = await Runner.run(
        selected_agent,
        runner_input,
    )

    return result.final_output
