from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using subprocess.run with shlex
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, check=True, capture_output=True)
    return {"status": "completed", "output": result.stdout.decode()}