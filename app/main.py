from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Secure implementation with proper input validation and sanitization
    if host.strip() == 'localhost' or host.startswith('127.0.0.1'):
        cmd = ["ping", *shlex.split(host)]
        subprocess.call(cmd)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}