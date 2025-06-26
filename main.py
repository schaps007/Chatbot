from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from chatbot import chatbot_response

app = FastAPI()

class Message(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: Request, msg: Message):
    api_key = request.headers.get("Authorization", "").replace("Bearer ", "")
    reply = chatbot_response(msg.message, api_key)
    return {"reply": reply}

@app.get("/", response_class=HTMLResponse)
async def serve_index():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()
