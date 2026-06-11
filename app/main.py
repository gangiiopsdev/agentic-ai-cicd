from fastapi import FastAPI
import subprocess
from pydantic import validator
from typing import Optional

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    @validator('host')
    def validate_host(cls, v):
        if not v.startswith('192.168.') and not v.startswith('localhost'):
            raise ValueError('Invalid host')
        return v

    try:
        output = subprocess.check_output(['ping', v], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}