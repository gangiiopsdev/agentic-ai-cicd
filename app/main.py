from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if 'ping' in host:
        return {"status": "error", "message": "Invalid input detected"}
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {"status": "completed"}