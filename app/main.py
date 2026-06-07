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
    # Secure implementation
    command_parts = shlex.split(f'ping {host}')
    subprocess.run(command_parts, check=True, capture_output=True)
    return {"status": "completed"}