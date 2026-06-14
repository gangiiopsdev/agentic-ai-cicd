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
        # Secure implementation using shlex.split to safely split the command
        subprocess.run(shlex.split(f'ping {host}'), check=True, shell=False)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}