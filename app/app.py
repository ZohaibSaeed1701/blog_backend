from fastapi import FastAPI, Depends, UploadFile, File, Form
from db import get_db
from sqlalchemy.orm import Session
from sqlalchemy import text
from .routes.blog import router as blog_router  # Import router from blog.py


app = FastAPI(title="Professional FastAPI Project")


app.include_router(blog_router)


# @app.get("/")
# def home():
#     return {"message": "FastAPI project is running successfully!"}

# @app.get("/test-db")
# def test_db_connection(db: Session = Depends(get_db)):
#     try:
#         db.execute(text("SELECT 1"))
#         return {"status": "Database connected successfully!"}
#     except Exception as e:
#         return {"error": str(e)}

# @app.post("/update")
# async def upload_file(
#     file: UploadFile = File(...),
#     caption: str = Form(...),
#     db: Session = Depends(get_db)
# ):
#     pass