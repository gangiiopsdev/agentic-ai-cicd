from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

def get_ip(host: str) -> Optional[dict]:
    if not host.isalnum():
        return {'error': 'Invalid hostname'}
    result = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode() if result.stderr else ''}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return get_ip(host)