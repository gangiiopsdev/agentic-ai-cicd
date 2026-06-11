from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

allowed_hosts = ['example.com', 'localhost']

def validate_host(host: str):
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str = validator(allowed_hosts)(str)):
    result = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}