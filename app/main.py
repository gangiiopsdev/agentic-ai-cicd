from fastapi import FastAPI
import subprocess
from fastapi.exceptions import HTTPException

def secure_ping(host: str):
    # Validate the host input to prevent command injection
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._')
    if not all(c in allowed_chars for c in host):
        raise ValueError('Invalid host format')
    result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        return secure_ping(host)
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=400, detail=str(e))