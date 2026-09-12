from fastapi import FastAPI
from pydantic import BaseModel, Field

from src.rag.pipeline import answer_question


app = FastAPI(
    title="ResolveAI API",
    description="AI-powered SAP SuccessFactors LMS troubleshooting assistant",
    version="1.0.0"
)


class QuestionRequest(BaseModel):
    question: str


class SourceCitation(BaseModel):
    source: str
    scenario: str
    category: str
    match_score: float


class QuestionResponse(BaseModel):
    answer: str
    sources: list[SourceCitation] = Field(default_factory=list)


@app.get("/")
def home():
    return {
        "message": "ResolveAI API is running successfully."
    }


@app.post("/ask", response_model=QuestionResponse)
def ask_question(request: QuestionRequest):
    result = answer_question(request.question)
    return result