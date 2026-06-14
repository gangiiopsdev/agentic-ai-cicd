from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str
    
    @validator('host')
    def validate_host(cls, v):
        if not v.startswith('192.168.') and not v.startswith('10.'):  # Example validation logic
            raise ValueError('Invalid IP address format')
        return v

@app.get("/ping")
def ping(request: PingRequest):
    response = subprocess.run(['ping', request.host], capture_output=True, text=True)
    return {'status': 'completed', 'output': response.stdout}