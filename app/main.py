from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    allowed_hosts = ['example.com', 'test.com']  # List of allowed hosts
    if host in allowed_hosts:
        command = shlex.split(f'ping {host}')
        result = subprocess.run(command, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        raise ValueError('Unauthorized host')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        return safe_ping(host)
    except ValueError as e:
        return {'error': str(e)}