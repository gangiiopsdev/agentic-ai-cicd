from fastapi import FastAPI
import subprocess
from shlex import quote
from pydantic import validator

app = FastAPI()

class HostValidator:
    @validator('host')
    def validate_host(cls, v):
        if not v.isalnum():
            raise ValueError('Invalid input')
        return v

@app.get("/ping")
def ping(host: str = Depends(HostValidator.validate_host)):
    try:
        result = subprocess.run(['ping', quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}