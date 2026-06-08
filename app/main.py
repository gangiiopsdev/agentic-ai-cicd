from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping {host}'
app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the input to ensure it is safe for use in a shell command
    if not host.isalnum() or '..' in host:
        raise ValueError('Invalid host name')
    command = generate_ping_command(host)
    subprocess.call(command, shell=False)
    return {'status': 'completed'}