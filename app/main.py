from fastapi import FastAPI
import subprocess
from pydantic import validator




class PingRequest(BaseModel):
    host: str
    @validator('host')
    def validate_host(cls, v):
        if not v.strip().replace('.', '').isalnum() or '.' not in v:
            raise ValueError('Invalid hostname')
        return v

app = FastAPI()

@app.get("/ping")
def ping_endpoint(request: PingRequest):
    host = request.host
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {'status': 'completed'}