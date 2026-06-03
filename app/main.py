from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent injection attacks
    if not all(c.isalnum() or c in ('-', '.', '_') for c in host):
        return {"status": "error", "message": "Invalid host parameter"}
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}