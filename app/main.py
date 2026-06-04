from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Ensure host is sanitized or validated before passing it to ping
    allowed_hosts = ['example.com', 'test.com']  # Replace with actual validation logic
    if host in allowed_hosts:
        subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)