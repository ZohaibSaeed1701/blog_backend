from fastapi import FastAPI, HTTPException

app = FastAPI(title="Simple FastAPI Project")

data = {1: {"data": "This is first"}, 2: {"data": "This is second"}}

@app.get("/test")
def test():
    return data

@app.get("/test/{id}")
def testing(id: int):
    if id not in data:
        raise HTTPException(status_code=401, detail="This id not found")
    return data.get(id)

@app.post("/test/{id}")
def test(id: int):
    if id not in data:
        raise HTTPException(status_code=401, detail="This id not found")
    return data.get(id)
