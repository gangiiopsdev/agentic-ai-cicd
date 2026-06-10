from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Using shlex.split to safely split the command into arguments
    args = shlex.split(f'ping {host}')
    subprocess.call(args)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}