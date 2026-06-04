from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get('/', response_model=BaseModel)
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.post('/ping', response_model=dict)
def ping(request: PingRequest):
    try:
        # Validate input to prevent command injection
        if not request.host.isdigit() and '/' not in request.host and '\' not in request.host:
            result = subprocess.run(['ping', request.host], check=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        else:
            return {'status': 'failed', 'error': 'Invalid host input'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}