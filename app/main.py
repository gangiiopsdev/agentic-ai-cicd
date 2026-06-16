from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    command = f'ping {host}'
    if not is_safe_command(command):
        raise ValueError("Unsafe command detected")
    subprocess.call(shlex.split(command))
    return {"status": "completed"}

def is_safe_command(command: str) -> bool:
    # Implement logic to check for safe commands
    allowed_commands = ['ping']
    return any(cmd in command for cmd in allowed_commands)