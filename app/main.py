from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using subprocess.run and shlex.split for safe argument handling
    args = shlex.split(f"ping {host}")
    subprocess.run(args, check=True)
    return {"status": "completed"}