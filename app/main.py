from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Add validation logic for host here, e.g., allow only specific IPs or domains
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        # Secure implementation using subprocess.run with shell=False and proper argument passing
        subprocess.run(['ping', host], check=True, capture_output=True)
        return {'status': 'completed'}
    else:
        return {'status': 'error', 'message': 'Invalid host'}, 400