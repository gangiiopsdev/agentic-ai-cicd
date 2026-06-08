from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class PingRequest(BaseModel):
    host: str
    @validator('host')
    def validate_host(cls, v):
        if any(char in v for char in '!@#$%^&*()_+-=[]{}|;:,.<>?`~'):  # Example validation
            raise ValueError('Invalid characters in hostname')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.post('/ping', response_model=dict)
def ping(request: PingRequest):
    try:
        result = subprocess.run(['ping', request.host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}