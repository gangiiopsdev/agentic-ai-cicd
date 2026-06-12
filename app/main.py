from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v or len(v) > 255:
            raise ValueError('Invalid host input')
        return v

@app.get('/ping', response_model=BaseModel)
def ping(request: PingRequest):
    result = subprocess.run(['ping', request.host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}