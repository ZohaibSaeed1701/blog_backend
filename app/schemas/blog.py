from pydantic import BaseModel

class PostBlog(BaseModel):
    context: str


class GetBlog(BaseModel):
    context: str
    embedding: str


    class Config:
        orm_mode: True