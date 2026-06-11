from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_command(command):
    # Validate and sanitize the command input
    if not command.startswith('ping '):
        raise ValueError("Invalid command")
    args = shlex.split(command)
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get="/ping")
def ping(host: str):
    command = f'ping {host}'
    return run_command(command)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}