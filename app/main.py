from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using shlex.split to avoid injection
    import shlex
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {"status": "completed"}