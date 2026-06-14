from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Secure implementation with input validation and sanitization
    valid_hosts = ['192.168.1.1', '10.0.0.1']  # Example allowed hosts
    if host not in valid_hosts:
        return {'status': 'failed', 'error': 'Invalid host'}
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and sanitization
    valid_hosts = ['192.168.1.1', '10.0.0.1']  # Example allowed hosts
    if host not in valid_hosts:
        return {'status': 'failed', 'error': 'Invalid host'}
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}