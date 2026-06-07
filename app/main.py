from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_host = subprocess.list2cmdline([host])
    args = shlex.split(f'ping {safe_host}')
    subprocess.run(args, check=True)

    return {"status": "completed"}