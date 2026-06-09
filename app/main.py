from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    command = shlex.split(f'ping {host}')
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}

    return {"status": "completed"}