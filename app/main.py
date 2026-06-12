from fastapi import FastAPI
import subprocess
from shlex import quote
generate_ping_command = lambda host: f'ping {quote(host)}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid host'}, 400
    subprocess.run(generate_ping_command(host), shell=False, check=True)
    return {'status': 'completed'}