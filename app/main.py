from fastapi import FastAPI
import subprocess
from pydantic import validator, BaseModel

global_ping = ["ping", "-c", "1"]

class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        if not v.isidentifier():  # Simple validation to avoid basic injection attacks
            raise ValueError('Invalid hostname')
        return subprocess.list2cmdline([v])  # Sanitize the host input

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.post('/ping')
def ping(request: PingRequest):
    subprocess.call(global_ping + [request.validate_host()])
    return {"status": "completed"}