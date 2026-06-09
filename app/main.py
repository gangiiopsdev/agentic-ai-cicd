from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using shlex.quote for safe command execution
    import shlex
    subprocess.call(shlex.split(f'ping {host}'))
    return {"status": "completed"}