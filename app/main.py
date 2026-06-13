from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not all(c.isalnum() or c in '-.' for c in v):
            raise ValueError('Invalid hostname')
        return v

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.call without shell=True
    args = ['ping', host]
    try:
        subprocess.run(args, check=True)
    except Exception as e:
        print(f"Error during ping: {e}")

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.post("/ping")
def ping(request: PingRequest):
    safe_ping(request.host)
    return {"status": "completed"}