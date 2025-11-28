from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import get_db
from ..schemas.blog import PostBlog, GetBlog
from ..models.blog import Blog
# Router object create karo
router = APIRouter()


# Example route
# @router.get("/blog")
# def get_blogs():
#     return {"message": "This is the blog list"}


# @router.get("/blog/{blog_id}")
# def get_blog(blog_id: int):
#     return {"message": f"This is blog number {blog_id}"}


@router.post("/create_blog", response_model=GetBlog)
async def create_blog(payload: PostBlog, db: Session = Depends(get_db)):
    db_data = Blog (
        context = payload.context,
        embedding = "Zohaib is the Best"
    )
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data