from fastapi import FastAPI
import subprocess
import shlex
def safe_command(command_parts):
    safe_parts = [shlex.quote(part) for part in command_parts]
    return ' '.join(safe_parts)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum() or len(host) > 10:
        return{'status': 'error', 'message': 'Invalid input'}, 400
    command_parts = ['ping'] + shlex.split(host)
    safe_command_str = safe_command(command_parts)
    result = subprocess.run(safe_command_str, capture_output=True, text=True, check=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}