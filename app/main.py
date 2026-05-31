from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    # Secure implementation using subprocess.run
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_api(host: str):
    return ping(host)