from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Validate and sanitize host input
    if not host or not all(c.isalnum() for c in host) or len(host) > 255:
        raise ValueError('Invalid host input')
    git_command = ['ping', host]
    subprocess.call(git_command)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        ping(host)
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}