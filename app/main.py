from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host parameter
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host) or len(host) > 255:
        return {'status': 'error', 'message': 'Invalid input'}
    subprocess.call(['ping', host])
    return {'status': 'completed'}