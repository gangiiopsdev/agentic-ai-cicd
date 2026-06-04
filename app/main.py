from fastapi import FastAPI
import subprocess
import shlex
globally_safe_hosts = ['127.0.0.1', '::1']  # List of safe hosts

app = FastAPI()

def sanitize_host(host):
    return host.strip() if host in globally_safe_hosts else None

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_host = sanitize_host(host)
    if safe_host:
        subprocess.run(['ping', *shlex.split(safe_host)], check=True, capture_output=True)
    else:
        return {'status': 'error', 'message': 'Unauthorized host'}

    return {'status': 'completed'}