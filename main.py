from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai_unofficial import OpenAIUnofficial

app = FastAPI()
client = OpenAIUnofficial()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat/")
async def chat_with_bot(request: ChatRequest):
    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": request.message}],
            model="gpt-3.5-turbo"
        )
        reply = response.choices[0].message.content
        return {"reply": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
