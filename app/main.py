from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command: str):
    result = subprocess.run(command.split(), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input before using it in a subprocess call
    if 'ping' not in host:
        return {'status': 'error', 'output': 'Invalid host'}
    command = ['ping', host]
    return execute_command(' '.join(command))