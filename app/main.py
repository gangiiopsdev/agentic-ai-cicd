from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate host input to prevent command injection
    if not host.replace('.', '').replace('-', '').isalnum():
        raise ValueError('Invalid hostname')
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {'status': 'completed'}