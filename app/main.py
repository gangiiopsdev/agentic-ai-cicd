from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command, params):
    # Validate and sanitize inputs
    for param in params:
        if not isinstance(param, str) or '&&' in param or ';' in param:
            raise ValueError('Invalid input parameter')
    return subprocess.run(command + list(params), capture_output=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input
    if not host or '&&' in host or ';' in host:
        raise ValueError('Invalid host parameter')
    command = ["ping", host]
    result = execute_command(command, [])
    return {"status": "completed", "output": result.stdout.decode() if not result.stderr else result.stderr.decode()}