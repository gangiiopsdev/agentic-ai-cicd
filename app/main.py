from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    if not all(c.isalnum() or c in [".", ":", "-"] for c in host):  # Allow only alphanumeric and safe characters
        return {'error': 'Invalid host parameter'}
    try:
        subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': e.output.decode()}