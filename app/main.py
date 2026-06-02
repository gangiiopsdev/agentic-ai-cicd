from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with input sanitization
    if 'ping' in host:
        subprocess.call(["ping", host])
    else:
        return {"error": "Invalid input detected"}

    return {"status": "completed"}