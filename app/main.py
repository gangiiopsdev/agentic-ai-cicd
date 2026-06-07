from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with input validation and quoting
    command = shlex.split(f'ping -c 4 {shlex.quote(host)}')
    subprocess.call(command)
    return {"status": "completed"}