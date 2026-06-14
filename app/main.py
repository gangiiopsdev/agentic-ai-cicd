from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate host input
    if not all(c.isalnum() or c in '.-' for c in host):
        raise ValueError('Invalid host name')
    # Safe implementation without shell=True
    subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}