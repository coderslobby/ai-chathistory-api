from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    answer: str
    created_at: datetime

class HistoryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    question: str
    answer: str
    created_at: datetime