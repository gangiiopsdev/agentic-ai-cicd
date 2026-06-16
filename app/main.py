from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Fixed implementation using subprocess.run and shlex.split for safe command execution
    args = shlex.split(f"ping {host}")
    result = subprocess.run(args, check=True)
    return {"status": "completed", "output": result.stdout.decode() if result.stdout else None}