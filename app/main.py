from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input to prevent command injection
    if not all(c.isalnum() or c in [".", "/"] for c in host):
        return {"status": "error", "message": "Invalid host name"}
    subprocess.call(["ping", host])
    return {"status": "completed"}