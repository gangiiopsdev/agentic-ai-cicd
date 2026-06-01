from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
def ping(host: str):
    # Sanitize input to prevent command injection
    sanitized_host = shlex.quote(host)
    command = ['ping', sanitized_host]
    subprocess.run(command, check=True)
    return {"status": "completed"}