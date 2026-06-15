from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent injection attacks
    if not host.isdigit() or len(host) > 15:
        return {'error': 'Invalid host'}, 400
    subprocess.run(['ping', f'127.0.0.1'], check=True, capture_output=True, shell=False)
    return {'status': 'completed'}