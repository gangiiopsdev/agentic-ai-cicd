from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not all(c.isalnum() or c in '.-' for c in v):
            raise ValueError('Invalid input')
        return v

@app.post("/ping")
def ping(request: PingRequest):
    args = ['ping', request.host]
    subprocess.run(args, check=True)
    return {"status": "completed"}