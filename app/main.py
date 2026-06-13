from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse

generate_ping_command = lambda host: f'ping {host}' if urlparse(host).hostname == 'localhost' else '/bin/false'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = generate_ping_command(host)
    if command == '/bin/false':
        return {'status': 'unauthorized'}
    result = subprocess.run(command.split(), check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}