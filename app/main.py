from fastapi import FastAPI
import subprocess
from fastapi import HTTPException

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.isalnum() or '.' not in host:
        raise HTTPException(status_code=400, detail='Invalid host format')
    subprocess.run(['ping', host], check=True, timeout=5)
    return {'status': 'completed'}