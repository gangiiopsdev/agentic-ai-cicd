from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        if 'localhost' not in v and '127.0.0.1' not in v:
            raise ValueError('Only localhost is allowed')
        return v

@app.get("/ping")
def ping(request: PingRequest):
    subprocess.call(['ping', request.host])
    return {"status": "completed"}