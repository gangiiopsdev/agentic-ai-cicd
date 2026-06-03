from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, value):
        if not value.startswith('127.0.0.1') and not value.startswith('localhost'):
            raise ValueError('Invalid host address')

@app.get("/ping")
def ping(request: PingRequest):
    subprocess.call(['ping', request.host])
    return {"status": "completed"}