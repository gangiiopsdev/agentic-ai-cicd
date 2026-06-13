from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

generate_ping_command = lambda host: ['ping', host]

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if any(char in v for char in ['&&', ';', '|', '>', '<']):
            raise ValueError('Invalid characters detected in host input')
        return v

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.post('/ping')
def ping(request: PingRequest):
    subprocess.run(generate_ping_command(request.host), check=True, shell=False)
    return {'status': 'completed'}