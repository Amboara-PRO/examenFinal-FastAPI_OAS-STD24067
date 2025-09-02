from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/ping")
def ping():
    return JSONResponse(content="pong", status_code=200)
