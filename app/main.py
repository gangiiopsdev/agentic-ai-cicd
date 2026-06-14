from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    args = shlex.split(f'ping {host}')
    # Sanitize input to prevent injection
    if not all(c.isalnum() or c in (',', '.', '-', '_') for c in host):
        raise ValueError('Invalid host input')
    subprocess.run(args, check=True)
    return {"status": "completed"}