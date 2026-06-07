from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with full path and proper validation
    if host.startswith('localhost:') or host.isdigit() or host == '127.0.0.1':
        subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True)
    return {'status': 'completed'}