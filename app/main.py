from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if validate_host(host):
        args = ['ping', host]
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 400

def validate_host(host: str) -> bool:
    # Implement a simple validation to allow only alphanumeric characters and dots
    import re
    pattern = r'^[a-zA-Z0-9.]+$'
    return re.match(pattern, host) is not None