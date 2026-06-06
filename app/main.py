from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    if not host.isalnum() or len(host) > 50:
        return False
    return True

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'error': 'Invalid hostname'}
    args = ['ping', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True, shell=False)
    return {
        'status': 'completed',
        'output': result.stdout,
    }