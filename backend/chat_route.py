from fastapi import APIRouter

from schemas import ChatRequest, ChatResponse
from agent_service import handle_chat


router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    response = await handle_chat(request.message, request.messages)
    return ChatResponse(response=response)
