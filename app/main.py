from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if host not in ['127.0.0.1', '::1']:  # Add more validation as needed
        return {'error': 'Invalid host'}, 400
    subprocess.run(['ping', '-c', '1', host], check=True)
    return {'status': 'completed'}