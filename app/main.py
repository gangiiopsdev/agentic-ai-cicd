from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel

class SafeSubprocess:
    @staticmethod
def call(command: str, *args, **kwargs):
        args = shlex.split(command)
        return subprocess.call(args, *args, **kwargs)

class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.post("/ping")
def ping(request: PingRequest):
    command = f'ping {shlex.quote(request.host)}'
    SafeSubprocess.call(command)
    return {"status": "completed"}