from fastapi import FastAPI
import subprocess
import shlex
generate_ping_command = lambda host: f'ping {host}'
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    # Safe implementation
    command_parts = shlex.split(generate_ping_command(host))
    subprocess.call(command_parts)
    return {'status': 'completed'}