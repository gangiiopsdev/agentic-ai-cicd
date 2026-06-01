from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input
    if not host.isdigit() or len(host) > 3:
        raise ValueError("Invalid host")
    command = shlex.split(f'ping {host}')
    subprocess.run(command, check=True, stdout=subprocess.PIPE)
    return {"status": "completed"}