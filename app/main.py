from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping {host}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to ensure it does not contain malicious content
    if not host.isalnum() and not all(c in string.digits for c in host):
        raise ValueError('Invalid host parameter')
    subprocess.call(generate_ping_command(host), shell=False)
    return {'status': 'completed'}