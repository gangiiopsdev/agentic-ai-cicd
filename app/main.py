from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Simple example of validation: check if the host contains only alphanumeric characters and hyphens
    return all(c.isalnum() or c == '-' for c in host)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if validate_host(host):  # Validate the input before use
        args = ['ping', host]
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 400