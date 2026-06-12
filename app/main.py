from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input
    if not host.isalnum():
        return {"status": "failed", "error": "Invalid input"}
    subprocess.call(["ping", host])
    return {"status": "completed"}