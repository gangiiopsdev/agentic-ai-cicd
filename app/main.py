from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.post('/ping')
def ping(request: PingRequest):
    if not request.host.isalnum():  # Simple validation, improve for real-world use
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        result = subprocess.run(['ping', request.host], capture_output=True, text=True, timeout=5)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

@app.post('/ping_safe')
def ping_safe(request: PingRequest):
    if not request.host.isalnum():  # Simple validation, improve for real-world use
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        result = subprocess.run(['ping', request.host], capture_output=True, text=True, timeout=5)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}