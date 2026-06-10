from fastapi import FastAPI
import os
import ping3
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    response_time = ping3.ping(request.host)
    if response_time is not None:
        return {"status": "completed", "response_time": response_time}
    else:
        return {"status": "failed"}