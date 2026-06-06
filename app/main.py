from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent shell injection
    if not host.isalnum() or '@' in host:
        return {'error': 'Invalid hostname'}, 400

    # Secure implementation with proper validation
    subprocess.run(['ping', '-c', '1', host], check=True)

    return {'status': 'completed'}