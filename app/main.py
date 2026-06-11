from fastapi import FastAPI
import shlex
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using shlex.split to avoid command injection
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {"status": "completed"}