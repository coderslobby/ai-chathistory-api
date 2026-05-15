from app.dbConnection import engine, sesionlocal, Base
from app.models import ChatRequest, ChatResponse, HistoryResponse
from app.dbTableStructure import chatHistory
from fastapi import FastAPI
from app.services.llm_call import chat_request
from datetime import datetime
from typing import List

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.post('/chat/')
def chat(request: ChatRequest) -> ChatResponse:
    answer = chat_request(request.question)
    db = sesionlocal()
    record = chatHistory(question=request.question,answer=answer)
    response = ChatResponse(answer=answer,created_at=datetime.now())
    try:
        db.add(record)
        db.commit()
    finally:
        db.close
    return response

@app.get('/history/')
def chat_history()-> List[HistoryResponse]:
    db = sesionlocal()
    try:
        records = db.query(chatHistory).all()
        print(records[0])
        return records
    finally:
        db.close()