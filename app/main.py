from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.strip() or len(v) > 255:
            raise ValueError('Invalid host name')
        return v

@app.post('/ping', response_model=str)
def ping_route(request: PingRequest):
    subprocess.run(['ping', request.host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)