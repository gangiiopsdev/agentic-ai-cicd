from fastapi import FastAPI
import subprocess

def execute_command(command: str):
    # Validate and sanitize input before execution
    if not command.startswith('ping'):
        raise ValueError("Invalid command")
    try:
        result = subprocess.run(command.split(), check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr

global app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = f'ping {host}'
    output = execute_command(command)
    return {"status": "completed", "output": output}