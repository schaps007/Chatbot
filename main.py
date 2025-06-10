

from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import chatbot_response

app = FastAPI()

class Message(BaseModel):
    message: str

@app.post("/chat")
async def chat(msg: Message):
    reply = chatbot_response(msg.message)
    return {"reply": reply}
