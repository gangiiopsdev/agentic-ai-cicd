from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with shell=False and input validation
    if not host.isalnum() or '.' not in host:
        raise ValueError("Invalid host address")
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)

    return {"status": "completed"}