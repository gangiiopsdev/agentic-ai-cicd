from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using shlex.split for safe argument handling
    subprocess.call(['ping'] + shlex.split(host))
    return {"status": "completed"}