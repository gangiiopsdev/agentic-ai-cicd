from fastapi import FastAPI, HTTPException
import subprocess
import shlex
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def check_host(cls, v):
        allowed_hosts = ['example.com', 'test.com']
        if v not in allowed_hosts:
            raise ValueError('Invalid host')
        return v

@app.post("/ping")
def ping_route(request: PingRequest):
    try:
        result = subprocess.run(['ping', request.host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=str(e))