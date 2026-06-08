from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

global pings = set()

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):