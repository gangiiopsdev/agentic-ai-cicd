from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with shell=False to avoid shell injection
    args = shlex.split(f'ping {host}')
    subprocess.call(args, shell=False)
    return {"status": "completed"}