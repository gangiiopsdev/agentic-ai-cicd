from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it does not contain malicious commands or paths
    if '/' in host or '\' in host or '..' in host:
        return {"status": "error", "message": "Invalid host name"}
    subprocess.call(["ping", host])
    return {"status": "completed"}