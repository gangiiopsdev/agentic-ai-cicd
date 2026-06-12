from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input to prevent injection attacks
    if not host.isalnum() or len(host) > 64:
        return {'status': 'error', 'error_message': 'Invalid host name'}
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error_message': str(e)}