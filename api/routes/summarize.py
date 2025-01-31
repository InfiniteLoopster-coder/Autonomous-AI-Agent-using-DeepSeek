from fastapi import APIRouter
import agents.assistant as assistant

router = APIRouter()

@router.post("/")
async def summarize_email(email: str):
    response = assistant.deepseek_assistant.generate(f"Summarize this email: {email}")
    return {"summary": response}
