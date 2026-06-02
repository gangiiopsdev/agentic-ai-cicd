from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with validation and sanitization
    if not host.isalnum() or len(host) > 100:
        raise ValueError("Invalid input for ping command")
    subprocess.run(shlex.split(f"ping {host}"), check=True)
    return {"status": "completed"}