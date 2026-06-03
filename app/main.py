from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host')
    def validate_host(cls, value):
        # Simple validation to prevent certain characters or patterns
        if any(char in '!@#$%^&*()_+{}|:"<>?/\`~' for char in value):
            raise ValueError('Invalid host name')
        return value

@app.get("/ping")
def ping(request: PingRequest):
    try:
        output = subprocess.check_output(['ping', request.host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}