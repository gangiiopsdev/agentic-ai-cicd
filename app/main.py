from fastapi import FastAPI
import subprocess
import shlex
def run_safe_command(command_parts):
    try:
        result = subprocess.run(command_parts, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Command failed: {e.stderr}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() and '-' not in host:
        return {'error': 'Invalid input'}, 400
    safe_command = ['ping', shlex.quote(host)]
    return run_safe_command(safe_command)