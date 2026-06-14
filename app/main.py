from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.isalnum():
        raise ValueError("Invalid input")
    command_parts = ['ping', shlex.quote(host)]
    subprocess.run(command_parts, check=True)
    return {"status": "completed"}