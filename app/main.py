from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator
def safe_ping(host):
    allowed_hosts = ['localhost', '127.0.0.1']
    if host not in allowed_hosts:
        raise ValueError('Only localhost is allowed')
    return host
app = FastAPI()
class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        return safe_ping(v)
@app.get("/ping")
def ping(request: PingRequest):
    subprocess.call(['ping', request.host])
    return {"status": "completed"}