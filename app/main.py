from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate host input to ensure it only contains allowed characters
    if not host.isalnum() and '-' in host:
        return {'status': 'failed', 'error': 'Invalid host input'}

    try:
        subprocess.run(['ping', host], check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

    return {'status': 'completed'}