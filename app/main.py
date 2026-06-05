from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        if not v.isalnum() or '-' not in v or '.' in v:
            raise ValueError('Invalid input')
        return v

@app.post('/ping')
def ping(request: PingRequest):
    args = ['ping', f'-c 1 {request.host}']
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}