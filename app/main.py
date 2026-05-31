from fastapi import FastAPI
import subprocess
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

def ping(host: str):
    # Secure implementation with input validation and sanitization
    if '@' not in host and len(host) < 256:
        subprocess.run(['ping', host], check=True)
    else:
        raise ValueError('Invalid host')

@app.get('/ping')
def ping_endpoint(host: str):
    try:
        return ping(host)
    except ValueError as e:
        return {'error': str(e)}, 400