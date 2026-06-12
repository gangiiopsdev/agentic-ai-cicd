from fastapi import FastAPI
import subprocess
from pydantic import validator, BaseModel

class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        # Implement proper validation logic here
        allowed_hosts = ['localhost', '127.0.0.1']
        if v not in allowed_hosts:
            raise ValueError(f'Host {v} is not allowed')
        return v

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    # Secure implementation
    subprocess.call(['ping', request.host])
    return {"status": "completed"}