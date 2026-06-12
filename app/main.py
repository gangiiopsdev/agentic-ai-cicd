from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Secure implementation using subprocess.run with shell=False
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host name')
    return safe_ping(host)

def validate_host(host):
    # Add validation logic here to ensure the host is safe to ping
    allowed_hosts = ['example.com', '127.0.0.1']
    return host in allowed_hosts