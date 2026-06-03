from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, value):
        if not value.isalnum():
            raise ValueError('Invalid host name')
        return value

@app.get("/ping")
def ping(request: PingRequest):
    args = ['ping', request.host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}