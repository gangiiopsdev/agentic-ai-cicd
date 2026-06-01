from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True, shell=False)  # Set shell=False to prevent shell injection
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}