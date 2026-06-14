from fastapi import FastAPI
import subprocess
def execute_safe_command(command: str):
    # Execute command safely without using shell=True and validate/sanitize input
    if not all(c.isalnum() or c in [' ', '-'] for c in command):  # Example validation, adjust as needed
        raise ValueError('Invalid characters in command')
    subprocess.run(command.split(), check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with validation
    execute_safe_command(f'ping {host}')
    return {"status": "completed"}