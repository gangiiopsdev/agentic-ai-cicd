from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum() or '.' not in host:
        return {"status": "invalid_host"}
    args = ['ping', host]
    subprocess.call(args, shell=False)
    return {"status": "completed"}