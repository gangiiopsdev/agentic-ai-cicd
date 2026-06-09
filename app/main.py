from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    if host in allowed_hosts:
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, check=True, capture_output=True)
        return {'status': 'completed', 'output': result.stdout.decode()}
    else:
        raise ValueError('Host not allowed')

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