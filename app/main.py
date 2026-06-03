from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with validation and sanitization
    if host.isalnum():
        subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid input for host')
    return {"status": "completed"}