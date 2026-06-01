from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation with validation and sanitization
    if not host.isalnum():
        return {'error': 'Invalid input', 'status': 'failed'}
    args = ['ping', shlex.quote(host)]
    try:
        subprocess.call(args)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e), 'status': 'failed'}