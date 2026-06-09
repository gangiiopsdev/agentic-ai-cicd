from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if host == 'localhost' or host == '127.0.0.1':
        subprocess.run(['ping', host], check=True, capture_output=True)
    else:
        return {'status': 'denied'}
    return {'status': 'completed'}