from fastapi import FastAPI
import subprocess
from pydantic import validator

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.startswith(('192.', '172.', '10.')):  # Example validation
            raise ValueError('Invalid host')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.post('/ping', response_model=PingRequest)
def ping(request: PingRequest):
    subprocess.run(['ping', request.host], check=True, timeout=5)
    return {'status': 'completed'}