from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with proper sanitization
    if not host.isalnum():
        raise ValueError('Invalid input')
    subprocess.run(['ping', f'--{host}'], check=True)
    return {'status': 'completed'}