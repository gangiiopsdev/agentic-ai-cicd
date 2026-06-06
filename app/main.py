from fastapi import FastAPI
import subprocess
import shlex
generate_ping_command = lambda host: f'ping {host}' if len(host.split()) == 1 else None
def safe_generate_ping_command(host):
    command_parts = shlex.split(generate_ping_command(host))
    return ['ping'] + command_parts
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    if len(host.split()) == 1:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'error': 'Invalid host parameter'}, 400