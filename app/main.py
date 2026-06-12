from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.startswith('localhost') and not host.startswith('127.0.0.1'):
        return {"error": "Invalid host"}
    try:
        command_parts = shlex.split(f'ping {host}')
        subprocess.run(command_parts, check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}