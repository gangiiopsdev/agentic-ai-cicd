from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping {host}' if len(host.split()) == 1 else None

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = generate_ping_command(host)
    if command is not None:
        subprocess.call(command, shell=False)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host parameter'}, 400