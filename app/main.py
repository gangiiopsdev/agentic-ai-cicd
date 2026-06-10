from fastapi import FastAPI
import subprocess
import shlex
import re

def execute_safe_command(command: str):
    try:
        # Validate the input to prevent command injection
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid host')
        args = shlex.split(command)
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    except (subprocess.CalledProcessError, ValueError) as e:
        return f'Error: {e.stderr}'

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = f'ping {host}'
    output = execute_safe_command(command)
    return {'status': 'completed', 'output': output}