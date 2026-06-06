from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if '@' in host or '&' in host or ';' in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    args = ['ping', shlex.quote(host)]
    subprocess.call(args)
    return {'status': 'completed'}