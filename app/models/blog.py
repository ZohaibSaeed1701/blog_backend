from sqlalchemy import Column, String, Text
from db import Base, engine  
import uuid

class Blog(Base):
    __tablename__ = "blog"
    id = Column(String, primary_key=True, index=True, default = lambda: str(uuid.uuid4()))
    context = Column(Text, nullable=False)
    embedding = Column(Text, index=True, nullable=False)


Base.metadata.create_all(bind=engine)
