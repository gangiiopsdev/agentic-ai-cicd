from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.post("/ping", response_model=PingRequest)
def ping(host: str):
    # Safe implementation using parameterized command
    subprocess.call(["ping", host])
    return {"status": "completed"}