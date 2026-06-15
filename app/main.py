from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with proper argument handling
    command = shlex.split(f'ping {host}')
    subprocess.run(command, check=True)
    return {"status": "completed"}