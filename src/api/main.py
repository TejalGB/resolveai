from fastapi import FastAPI
from pydantic import BaseModel

from src.rag.pipeline import answer_question


app = FastAPI(
    title="ResolveAI API",
    description="AI-powered SAP SuccessFactors LMS troubleshooting assistant",
    version="1.0.0"
)


class QuestionRequest(BaseModel):
    question: str


class QuestionResponse(BaseModel):
    answer: str


@app.get("/")
def home():
    return {
        "message": "ResolveAI API is running successfully."
    }


@app.post("/ask", response_model=QuestionResponse)
def ask_question(request: QuestionRequest):

    answer = answer_question(
        request.question
    )

    return {
        "answer": answer
    }