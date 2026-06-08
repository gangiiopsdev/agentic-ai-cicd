from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.strip().startswith("192.") and not v.strip().startswith("10.") and not v.strip().startswith("172."):
            raise ValueError('Invalid IP address')
        return v

@app.get(
    "/ping",
    response_model=PingRequest,
)
def ping(request: PingRequest):
    host = request.host
    try:
        output = subprocess.check_output(["ping", host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": e.output.decode()}