from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    if host.startswith('localhost') or host.startswith('127.0.0.1'):
        return subprocess.call(['ping', host])
    else:
        raise ValueError("Invalid host")

app = FastAPI()

@app.get="/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    return {"status": run_ping(host)}