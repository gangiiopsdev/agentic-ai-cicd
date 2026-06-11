from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not all(c.isalnum() or c in ['-', '.', '_'] for c in v):
            raise ValueError('Invalid characters in hostname')
        return v

@app.get("/ping")
def ping(request: PingRequest):
    args = ['ping', request.host]
    subprocess.call(args)
    return {"status": "completed"}