from sqlalchemy import Column, Integer, Text
from db import Base, engine  


class Blog(Base):
    __tablename__ = "blog"
    id = Column(Integer, primary_key=True, index=True)
    context = Column(Text, nullable=False)
    embedding = Column(Text, index=True, nullable=False)


Base.metadata.create_all(bind=engine)
