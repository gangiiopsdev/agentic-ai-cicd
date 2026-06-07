from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

class PingRequest(BaseModel):
    host: str
    @validator('host')
    def validate_host(cls, v):
        allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._')
        if not all(c in allowed_chars for c in v):
            raise ValueError('Host contains disallowed characters')
        return v

app = FastAPI()
@app.post('/ping', response_model=dict)
def ping(request: PingRequest):
    sanitized_host = request.host.replace(';', '').replace('&', '').replace('$', '')  # Additional mitigation
    args = ['ping', sanitized_host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}