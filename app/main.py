from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}

def is_valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., allow only specific hosts or IPs
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts