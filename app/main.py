from fastapi import FastAPI
import subprocess
import shlex
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host')
    def validate_host(cls, value):
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
        if not all(char in allowed_chars for char in value):
            raise ValueError('Invalid characters in host name')
        return value

@app.get('/ping', response_model=PingRequest)
def ping(request: PingRequest): 
    sanitized_host = shlex.quote(request.host)
    args = ['ping', sanitized_host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}