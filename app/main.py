from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host.isalnum() and len(host) <= 255:
        command = shlex.split(f'ping {host}')
        subprocess.call(command)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host input"}