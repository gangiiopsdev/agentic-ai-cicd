from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    if host.strip() == 'localhost' or host.strip().startswith('127.0.0.1'):
        subprocess.call(["ping", host])
    else:
        return {"status": "invalid host"}
    return {"status": "completed"}