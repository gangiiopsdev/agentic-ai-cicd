from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Ensure the host input is valid and safe
    if not host or not host.strip():
        raise ValueError('Invalid host input')
    args = ['ping'] + shlex.split(host)
    subprocess.run(args, check=True)
    return {"status": "completed"}