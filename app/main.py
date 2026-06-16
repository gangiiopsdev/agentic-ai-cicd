from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input before passing to subprocess
    if host.isalnum() and len(host) <= 32:
        subprocess.call(['ping', host])
        return {"status": "completed"}
    else:
        return {"error": "Invalid input"}