from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        output = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return ping(host)

def validate_host(host: str):
    allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    return host in allowed_hosts