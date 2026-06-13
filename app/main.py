from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    @validator('host')
    def validate_host(v):
        if v != 'localhost':
            raise ValueError('Only localhost is allowed for security reasons.')
        return v

    # Safe implementation
    subprocess.call(["ping", host])

    return {"status": "completed"}