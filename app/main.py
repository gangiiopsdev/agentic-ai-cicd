from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Sanitize input to prevent injection attacks
    if not host.strip().isdigit():
        return {'status': 'error', 'message': 'Invalid input'}
    subprocess.run(['ping', host], check=True, capture_output=True, text=True)
    return {'status': 'completed'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
ping