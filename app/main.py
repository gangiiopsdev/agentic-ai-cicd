from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.strip() or ' ' in host:
        return {"error": "Invalid input"}, 400
    command = shlex.split(f'ping {host}')
    subprocess.call(command)
    return {"status": "completed"}