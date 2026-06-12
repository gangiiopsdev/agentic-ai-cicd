from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using subprocess.run with shell=False and proper command construction
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, check=True, stdout=subprocess.PIPE)
    return {"status": "completed", "output": result.stdout.decode()}