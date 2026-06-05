from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Safe implementation with validation and sanitization
        if not host.isdigit():
            return {'status': 'failed', 'error': 'Invalid input'}
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/')
def root():
    return home()

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)