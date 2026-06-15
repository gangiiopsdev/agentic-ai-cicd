from fastapi import FastAPI
import subprocess
global_args = ['ping', '-c', '4']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with input validation
    if all(c in '0123456789.-' for c in host) and len(host.split('.')) == 4:
        subprocess.call(global_args + [host])
    else:
        return {'error': 'Invalid hostname'}

    return {'status': 'completed'}