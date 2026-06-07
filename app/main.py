from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host or not isinstance(host, str) or len(host) > 255:
        raise ValueError('Invalid host input')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {
        'status': 'completed',
        'stdout': result.stdout,
        'stderr': result.stderr
    }