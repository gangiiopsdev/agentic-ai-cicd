from fastapi import FastAPI
import subprocess
import shlex
global host
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run directly with user input
    command = f'ping -c 4 {host}'
    subprocess.run(command, shell=False, check=True)
    return {"status": "completed"}