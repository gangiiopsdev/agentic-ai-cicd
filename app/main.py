from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, value):
        if not value or ' ' in value:
            raise ValueError('Invalid host')
        return value

@app.get("/ping")
def ping(request: PingRequest):
    subprocess.call(['ping', request.host], shell=False)
    return {"status": "completed"}