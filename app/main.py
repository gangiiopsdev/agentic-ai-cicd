from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Validate and sanitize the host input
    if not host or len(host) > 255:
        return {'status': 'error', 'message': 'Invalid host'}
    return subprocess.call(['ping', host]) == 0

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    if result:
        return {'status': 'completed'}
    else:
        return {'status': 'error', 'message': 'Failed to ping host'}