from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from main import Chatbot

app = FastAPI()
chatbot = Chatbot()

class UserInput(BaseModel):
    user_input: str

@app.post("/chat/")
def chat(user_input: UserInput):
    question = chatbot.ask_question(user_input.user_input)
    # response = chatbot.respond(user_input.user_input)

    return {
        "question": question
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
