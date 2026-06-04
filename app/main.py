from fastapi import FastAPI
import subprocess
from pydantic import validator
from fastapi.exceptions import HTTPException

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to ensure it's safe for use with subprocess
    if not host.isalnum() or '.' not in host:
        raise HTTPException(status_code=400, detail='Invalid host format')

    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr}