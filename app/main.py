from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation
    @validator('host')
    def validate_host(value):
        if any(cmd in value for cmd in ['ping', '&&', '||', ';']):
            raise ValueError('Invalid host name or command injection attempt')
        return value
    subprocess.run(['ping', host], check=True, shell=False)
    return {'status': 'completed'}