from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

# Define a whitelist of allowed hosts for security reasons
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

def ping(host: str):
    if host not in ALLOWED_HOSTS:
        raise ValueError('Host is not allowed')
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)