from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        # Basic validation of the host name
        if not v.strip():
            raise ValueError('Host cannot be empty')
        return v

@app.post('/ping')
def ping(request: PingRequest):
    try:
        output = subprocess.check_output(['ping', request.host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'result': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return str(e.output)