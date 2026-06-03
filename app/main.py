from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with shlex for argument splitting
    if all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for c in host):  # Basic validation
        subprocess.call(shlex.split(f'ping {host}'))
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid hostname'}, 400