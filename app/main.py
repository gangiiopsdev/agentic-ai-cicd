from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not cls._is_safe_host(v):
            raise ValueError('Invalid host name')
        return v

    @staticmethod
def _is_safe_host(host):
        # Implement your logic to check if the host is safe
        return True

@app.get("/ping")
def ping(request: PingRequest):
    subprocess.call(["ping", request.host])
    return {"status": "completed"}