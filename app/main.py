from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Validate and sanitize the input before using it in subprocess
        allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
        if host not in allowed_hosts:
            raise ValueError('Invalid host')
        output = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Validate and sanitize the input before using it in subprocess
        allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
        if host not in allowed_hosts:
            raise ValueError('Invalid host')
        output = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}