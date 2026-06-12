from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with shell=False and using shlex.split to avoid command injection
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {"status": "completed"}