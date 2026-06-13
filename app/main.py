from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Define a whitelist of allowed hosts or patterns
    allowed_hosts = ['127.0.0.1', 'localhost']
    return host in allowed_hosts

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'failed', 'error': 'Unsafe host'}
    try:
        # Secure implementation using subprocess.run with shell=False and check=True
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}