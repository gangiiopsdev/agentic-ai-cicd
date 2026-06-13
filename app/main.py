from fastapi import FastAPI
import subprocess
from pydantic import validator

class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        if not all(c.isalnum() or c in ('.', '-', '_') for c in v):
            raise ValueError('Invalid hostname characters')
        return v

app = FastAPI()

@app.get('/ping', response_model=PingRequest)
def ping(request: PingRequest):
    sanitized_host = subprocess.quote(request.host)
    result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}