from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

class Cars(BaseModel):
    id: str
    brand: str
    model: str
    charasteristics: object

@app.get("/ping")
def ping():
    return JSONResponse(content="pong", status_code=200, content_type="text/plain")
@app.post("/cars")
def create_cars(request, response):
    # JSONResponse(content=)

@app.get("/cars")
def cars():
    return JSONResponse(content=Cars, status_code=200, content_type="application/json")

@app.get("/cars/{id}")
def get_cars(id: str):
    return JSONResponse(content=Cars, status_code=200, content_type="application/json")

@app.put("/cars/{id}/characteristics")
def update_cars(id: str, characteristics: object):
    return JSONResponse(content=Cars, status_code=200, content_type="application/json")