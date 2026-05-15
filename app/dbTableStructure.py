from sqlalchemy.orm import Mapped, mapped_column
from app.dbConnection import Base, engine
from datetime import datetime
from sqlalchemy import DateTime

class chatHistory(Base):
    __tablename__ = 'chatHistory'
    id: Mapped[int] = mapped_column(primary_key=True,nullable=False,autoincrement=True)
    question: Mapped[str] = mapped_column(nullable=False)
    answer: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)