from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_subprocess(command):
    args = shlex.split(command)
    subprocess.call(args)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    safe_subprocess(f'ping {host}')
    return {"status": "completed"}