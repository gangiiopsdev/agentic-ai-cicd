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
    # Secure implementation using shlex to safely handle user input
    command = f'ping {host}'
    args = shlex.split(command)
    subprocess.run(args, check=True)
    return {"status": "completed"}