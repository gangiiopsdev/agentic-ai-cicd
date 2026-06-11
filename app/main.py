from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.isdigit() or len(host) > 3:
        return {'error': 'Invalid host'}, 400
    subprocess.run(['ping', host], check=True, shell=False)