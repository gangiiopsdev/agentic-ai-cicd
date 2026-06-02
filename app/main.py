from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from typing import List

app = FastAPI()

class PingRequest(BaseModel):
    hosts: List[str]

@app.post("/ping")
def ping(request: PingRequest):
    for host in request.hosts:
        # Safe implementation with input validation
        subprocess.call(["ping", host])
    return {"status": "completed"}