from fastapi import FastAPI
import subprocess
from fastapi import HTTPException
import shlex
from pydantic import validator

class PingRequest(BaseModel):
    host: str
    @validator('host')
    def validate_host(cls, v):
        if not v.isalnum() or len(v) > 255:
            raise ValueError('Invalid host name')

app = FastAPI()

@app.get('/ping', response_model=PingRequest)
def ping(host: str):\n    command = ['ping', '-c', '1'] + shlex.split(host)
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return {'status': result.stdout.strip()}