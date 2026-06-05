from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    if not host.isdigit():
        raise ValueError('Invalid host input')
    ping_command = ['ping', '-c', '1', host]
    try:
        result = subprocess.run(ping_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    return result