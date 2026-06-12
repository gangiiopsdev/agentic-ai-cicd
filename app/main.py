from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum() or len(host) > 64:
        return {'error': 'Invalid input'}, 400
    args = ['ping', '-c', '1', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}