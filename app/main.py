from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to avoid injection vulnerabilities
    if not host.isalnum() and host != 'localhost':
        return {"status": "error", "message": "Invalid host parameter"}
    subprocess.call(["ping", host])
    return {"status": "completed"}