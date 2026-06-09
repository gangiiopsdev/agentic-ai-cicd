from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate the input to ensure it does not contain malicious characters
    if '&&' in host or '|' in host or ';' in host:
        raise ValueError('Invalid input detected')
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, timeout=5)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}