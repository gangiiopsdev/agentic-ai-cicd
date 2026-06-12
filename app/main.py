from fastapi import FastAPI
import subprocess
def secure_ping(host: str):
    # Validate and sanitize input
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid hostname')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and proper argument passing
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}