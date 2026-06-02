from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    if not host.isalnum() or len(host) > 64:
        raise ValueError('Invalid hostname')
    cmd = ['ping', '-c', '1', host]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        return execute_ping(host)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}