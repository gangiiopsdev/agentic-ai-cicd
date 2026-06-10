from fastapi import FastAPI
import subprocess

def run_ping(host: str):
    # Secure implementation
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.output)}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum() and not '.' in host:
        return {'status': 'failed', 'error': 'Invalid host format'}
    return run_ping(host)