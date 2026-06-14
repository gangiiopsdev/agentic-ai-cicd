from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    if not host.isalnum() or len(host) > 64:
        raise ValueError("Invalid host name")
    subprocess.call(['ping', host])
    return {"status": "completed"}