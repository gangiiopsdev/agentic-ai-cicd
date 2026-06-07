from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        # Simple validation to avoid shell injection
        if 'ping' in v or ';' in v:
            raise ValueError('Invalid host input')

@app.get("/ping")
def ping(request: PingRequest):
    subprocess.call(["ping", request.host])
    return {"status": "completed"}