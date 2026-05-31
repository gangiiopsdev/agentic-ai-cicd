from fastapi import FastAPI
import subprocess
import shlex

global host
host = None

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    command = shlex.split(f'ping {host}')
    subprocess.run(command, check=True)
    
    return {"status": "completed"}