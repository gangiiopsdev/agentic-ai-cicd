from fastapi import FastAPI
import subprocess
import shlex
gimport shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with input validation and sanitization
    if not host or '||' in host or ';' in host:
        return {"error": "Invalid input"}
    args = shlex.split(f'ping {host}')
    subprocess.call(args)

    return {"status": "completed"}