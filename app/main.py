from fastapi import FastAPI
import subprocess
from fastapi import HTTPException

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation and sanitization
    if not host.isalnum() or len(host) > 255:
        raise HTTPException(status_code=400, detail='Invalid hostname')
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}