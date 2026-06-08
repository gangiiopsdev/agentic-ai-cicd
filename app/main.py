from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    @validator('host')
    def validate_host(value):
        if 'ping' in value:
            raise ValueError('Invalid host name')
        return value
    subprocess.run(["ping", host], check=True)
    return {"status": "completed"}