from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        # Basic validation to ensure the input is not empty and does not contain potentially harmful characters
        if not v or not v.strip() or any(char in v for char in (';', '&', '|', '&&', '||')):
            raise ValueError('Invalid host')
        return v

@app.post('/ping')
def ping(request: PingRequest):
    safe_host = subprocess.list2cmdline([request.host])
    args = ['ping', safe_host]
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    if result.returncode == 0:
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'failed', 'error': result.stderr}