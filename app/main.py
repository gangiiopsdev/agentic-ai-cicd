from fastapi import FastAPI
import subprocess
from pydantic import validator

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with input validation and sanitization
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    subprocess.call(['ping', host])

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}