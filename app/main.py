from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping {host}' if 'localhost' in host or '127.0.0.1' in host else None
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    if 'localhost' not in host and '127.0.0.1' not in host:
        return {'error': 'Invalid host'}
    command = generate_ping_command(host)
    if command:
        subprocess.call(command, shell=False)
        return {'status': 'completed'}