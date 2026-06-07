from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping {host} -c 1'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        raise ValueError('Invalid input')
    subprocess.call(generate_ping_command(host), shell=False)
    return {'status': 'completed'}