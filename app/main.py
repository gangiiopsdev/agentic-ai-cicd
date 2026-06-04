from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not all(c.isalnum() or c in ('.', '-', '_') for c in v):
            raise ValueError('Invalid hostname')
        return v

@app.post("/ping")
def ping_host(request: PingRequest):
    subprocess.run(['ping', request.host], check=True)