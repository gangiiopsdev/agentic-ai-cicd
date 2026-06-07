from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_command(command_parts):
    try:
        output = subprocess.run(command_parts, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command_parts = shlex.split(f'ping {host}')
    return run_command(command_parts)