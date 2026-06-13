from fastapi import FastAPI
import subprocess
cimport os
import shlex

def execute_command(command: str):
    # Validate and sanitize input
    try:
        parts = shlex.split(command)
        if not parts or parts[0].startswith('-'):
            raise ValueError('Invalid command format')
        for part in parts:
            if '&&' in part or ';' in part or '|' in part:
                raise ValueError('Unsafe characters detected in command')
    except Exception as e:
        raise ValueError(f'Command validation failed: {e}')

    # Check if executable exists
    if not os.path.exists('/bin/' + parts[0]):
        raise ValueError('Executable does not exist')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = f'ping {host}'
    execute_command(command)
    return {"status": "completed"}