from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping(host: str):
    # Validate and sanitize input to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9]{1,255}$', host):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        # Safe implementation using subprocess.run without shell=True
        result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    # Validate and sanitize input to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9]{1,255}$', host):
        return {'status': 'failed', 'error': 'Invalid input'}
    return ping(host)