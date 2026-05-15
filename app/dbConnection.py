from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.settings import settings

engine = create_engine(settings.database_url)
sesionlocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass