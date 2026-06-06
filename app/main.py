from fastapi import FastAPI
import subprocess
def generate_ping_command(host):
    if 'localhost' in host or '127.0.0.1' in host:
        return f'ping {host}'
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = generate_ping_command(host)
    if command:
        result = subprocess.run(command, shell=False, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    return {'status': 'failed'}