from fastapi import FastAPI
import subprocess
from shlex import quote
from pydantic import validator

class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        if ' ' in v or '\' in v or ';' in v:
            raise ValueError('Invalid input')
        return v

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.post('/ping', response_model=dict)
def ping(request: PingRequest):
    try:
        safe_command = ['ping', request.host]
        output = subprocess.run(safe_command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}