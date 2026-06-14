from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and appropriate arguments
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_wrapper(host: str):
    # Validate host input to prevent injection attacks
    if not valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return ping(host)

def valid_host(host: str) -> bool:
    # Basic validation for demonstration purposes
    return all(c.isalnum() or c in ['-', '.', '_', '@'] for c in host)