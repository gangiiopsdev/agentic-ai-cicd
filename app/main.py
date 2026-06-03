from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
        if not all(char in allowed_chars for char in v):
            raise ValueError('Host contains invalid characters')
        return v

@app.post('/ping')
def ping(request: PingRequest):
    sanitized_host = request.host
    args = ['ping', sanitized_host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}