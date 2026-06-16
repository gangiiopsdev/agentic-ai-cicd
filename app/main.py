from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using shlex to escape command arguments
    safe_host = shlex.quote(host)
    command = ['ping', safe_host]
    subprocess.run(command, check=True)
    return {"status": "completed"}