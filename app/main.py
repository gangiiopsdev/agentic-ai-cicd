from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        allowed_hosts = ['example.com', 'test.com']  # Replace with actual validation logic
        if v not in allowed_hosts:
            raise ValueError(f'Host {v} is not allowed')
        return v

@app.get("/ping")
def ping(host: str = Depends(PingRequest)):
    # Secure implementation
    subprocess.call(["ping", host])
    return {"status": "completed"}