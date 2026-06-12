from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.isalnum() or len(v) > 10:
            raise ValueError('Invalid host')
        return v

@app.post("/ping")
def ping(request: PingRequest):
    command = ["ping", request.host]
    subprocess.run(command, check=True)
    return {"status": "completed"}