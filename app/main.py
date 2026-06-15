from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid host name')
    # Secure implementation using subprocess.run with argument list
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    if result.returncode != 0:
        return {'status': 'failed', 'error': result.stderr}
    return {'status': 'completed', 'message': 'Ping successful'}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Validate and sanitize input
        if not host.isalnum() or len(host) > 255:
            raise ValueError('Invalid host name')
        # Secure implementation using subprocess.run with argument list
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
        if result.returncode != 0:
            return {'status': 'failed', 'error': result.stderr}
        return {'status': 'completed', 'message': 'Ping successful'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}