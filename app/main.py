from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        command_parts = shlex.split(f'ping {host}')
        subprocess.run(command_parts, check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}