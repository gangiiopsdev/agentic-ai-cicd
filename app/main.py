from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not cls.is_valid_host(v):
            raise ValueError('Invalid host input')
        return v  # Do not use shlex.quote

    @staticmethod
def is_valid_host(host: str) -> bool:
    # Implement validation logic here (e.g., IP address format, domain name length)
    return True

@app.get('/ping')
def ping(request: PingRequest):
    result = subprocess.run(['ping', shlex.quote(request.host)], capture_output=True, text=True)
    return {'output': result.stdout}