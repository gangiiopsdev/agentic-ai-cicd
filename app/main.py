from fastapi import FastAPI
import subprocess
from typing import Optional
from pydantic import BaseModel
import threading

global ping_lock
ping_lock = threading.Lock()

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):