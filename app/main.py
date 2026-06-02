from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.call with args instead of shell=True
    if 'localhost' in host or '127.0.0.1' in host:
        subprocess.call(['ping', host])
    else:
        return {"error": "Invalid host"}

    return {"status": "completed"}