from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with full executable path and input validation
    if subprocess.call(['ping', '-c', '1', host]) == 0:
        return {"status": "completed"}
    else:
        return {"status": "failed", "message": "Ping failed for the given host"}