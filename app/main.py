from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(host: str) -> str:
    if not host.isalnum():
        raise ValueError('Invalid host')
    return host

def execute_command(command: str) -> None:
    args = shlex.split(command)
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    print(result.stdout)

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = f'ping {sanitized_host}'
    execute_command(command)
    return {'status': 'completed'}