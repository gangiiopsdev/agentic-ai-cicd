from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate input
    if not host.isalnum() or '..' in host:
        return {'status': 'failed', 'error': 'Invalid host'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, text=True, capture_output=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}