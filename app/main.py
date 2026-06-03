from fastapi import FastAPI
import subprocess

app = FastAPI()

global_args = ['ping', '{host}']

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize host input
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}, 400
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}
def validate_host(host: str) -> bool:
    # Simple validation example
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts