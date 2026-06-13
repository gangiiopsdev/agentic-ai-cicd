from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and absolute path
    if not host.startswith('localhost') or len(host) > 50:
        return {"status": "error", "message": "Invalid host parameter"}
    subprocess.call(["/usr/bin/ping", host])
    return {"status": "completed"}