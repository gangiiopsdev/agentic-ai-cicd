from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.run and avoiding shell=True
    subprocess.run(['ping', host], check=True)

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_safe(host: str):
    try:
        # Validate input to prevent command injection
        if not host.isalnum() and '.' not in host:
            raise ValueError('Invalid input for ping host')
        subprocess.run(['ping', host], check=True)
        return {'status': 'completed'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}