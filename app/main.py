from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with input validation and sanitization
    if '&&' in host or ';' in host or '|' in host:
        raise ValueError('Invalid characters detected in host parameter')
    subprocess.call(['ping', host])
    return {"status": "completed"}