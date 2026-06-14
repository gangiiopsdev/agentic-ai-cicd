from fastapi import FastAPI
import subprocess

app = FastAPI()

global_args = ['ping', '{host}']

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid host name')
    result = subprocess.run(global_args, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}