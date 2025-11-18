from fastapi import FastAPI

app = FastAPI(title="Simple FastAPI Project")

@app.get("/")
def read_root():
    return {"message": "Hello from app.py!"}

@app.get("/hello_world")
def get_user():
    return {"message": "Hello Word"}
