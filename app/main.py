from fastapi import FastAPI
import subprocess
import shlex
generate_ping_command = lambda host: f'ping {host}' if len(host.split()) == 1 else None

def safe_generate_ping_command(host):
    command_parts = shlex.split(generate_ping_command(host))
    return ' '.join(command_parts)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = safe_generate_ping_command(host)
    if command is not None:
        subprocess.call(command, shell=True)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host parameter'}, 400