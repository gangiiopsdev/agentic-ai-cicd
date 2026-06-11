from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using shlex.split to safely split the command
    args = ['ping'] + shlex.split(host)
    subprocess.run(args, check=True)
    return {"status": "completed"}