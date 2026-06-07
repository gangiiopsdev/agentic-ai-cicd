from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_command(command):
    return subprocess.run(command, capture_output=True, text=True, check=True)

def safe_ping(host):
    if not host.isalnum():
        raise ValueError('Invalid input for ping command')
    command = ['ping', host]
    result = run_command(command)
    return {'status': result.stdout, 'stderr': result.stderr}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        return safe_ping(host)
    except ValueError as e:
        return {'error': str(e)}