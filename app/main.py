from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Validate and sanitize the host input
    allowed_hosts = ['example.com', 'another-example.com']
    if host in allowed_hosts:
        subprocess.call(['ping', host])
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)