from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.isalnum() or len(host) > 64:
        return {'error': 'Invalid input for host'}

    try:
        subprocess.run(['ping', host], check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e.stderr)}

    return {'status': 'completed'}