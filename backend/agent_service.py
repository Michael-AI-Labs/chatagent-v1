import re

from agents import Runner

from chat_agent import (
    normal_agent,
    math_agent,
    time_agent,
    conversion_agent,
    search_agent,
)


def classify_request(message: str) -> str:
    message = message.lower()

    explicit_time_patterns = [
        r"\bwhat time is it\b",
        r"\bwhat day is it\b",
        r"\bwhat(?:'s| is) the date\b",
        r"\bcurrent time\b",
        r"\bcurrent date\b",
        r"\btoday'?s date\b",
    ]

    search_patterns = [
        r"\blatest\b",
        r"\bnews\b",
        r"\bweather\b",
        r"\btoday\b",
        r"\bcurrent\b",
        r"\bwho won\b",
        r"\bscore\b",
        r"\bscores\b",
        r"\bforecast\b",
        r"\bheadline[s]?\b",
        r"\brecent\b",
        r"\bsearch the web\b",
        r"\bsearch online\b",
        r"\blook it up\b",
        r"\bgame\b",
    ]

    math_patterns = [
        r"\bcalculate\b",
        r"\bplus\b",
        r"\bminus\b",
        r"\d+\s*[\+\-\*/]\s*\d+",
        r"=",
    ]

    time_patterns = [
        r"\btime\b",
        r"\bdate\b",
        r"\bday\b",
        r"\bclock\b",
    ]

    conversion_patterns = [
        r"\bconvert\b",
        r"\bkilometers?\b",
        r"\bmiles?\b",
        r"\bpounds?\b",
        r"\bkilograms?\b",
    ]

    if any(re.search(pattern, message) for pattern in explicit_time_patterns):
        return "time"

    if any(re.search(pattern, message) for pattern in search_patterns):
        return "search"

    if any(re.search(pattern, message) for pattern in math_patterns):
        return "math"

    if any(re.search(pattern, message) for pattern in time_patterns):
        return "time"

    if any(re.search(pattern, message) for pattern in conversion_patterns):
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

    elif classification == "search":
        selected_agent = search_agent

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
