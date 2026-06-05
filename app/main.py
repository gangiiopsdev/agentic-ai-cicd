from fastapi import FastAPI
import subprocess
from pydantic import validator

class PingRequest:
    host: str

    @validator('host', pre=True)
    def validate_host(cls, value):
        if not value.isalnum():
            raise ValueError("Invalid hostname")
        return value

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.post('/ping')
def ping(request: PingRequest):
    args = ['ping', '-c', '1', request.host]
    subprocess.call(args)
    return {'status': 'completed'}