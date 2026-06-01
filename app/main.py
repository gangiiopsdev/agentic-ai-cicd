from fastapi import FastAPI
import subprocess
from pydantic import validator, BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str
    
    @validator('host')
    def validate_host(cls, v):
        if not v.startswith('192.168.'):
            raise ValueError('Host must be in the 192.168.0.0/16 range')
        return v

@app.get("/ping")
def ping(request: PingRequest):
    try:
        output = subprocess.run(['ping', request.host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}