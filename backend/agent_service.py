from agents import Runner

from chat_agent import chat_agent


async def handle_chat(message: str) -> str:
    result = await Runner.run(chat_agent, message)
    return result.final_output