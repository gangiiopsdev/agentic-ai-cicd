from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize and validate the host input
    if not isinstance(host, str) or len(host.strip()) == 0:
        raise ValueError('Invalid or untrusted host')
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Invalid or untrusted host')

    # Use a safer approach to execute the command
    subprocess.run(['ping', '-c 4' if host == '127.0.0.1' else 'ping -6 -c 4', host], capture_output=True, text=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}