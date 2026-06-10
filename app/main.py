from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        # Basic validation to avoid common pitfalls like shell injection
        if '&&' in v or ';' in v or '&' in v:
            raise ValueError('Invalid input detected')
        return v

def safe_ping(host: str):
    args = ['ping', host]
    subprocess.call(args)

@app.get("/ping")
def ping(request: PingRequest):
    safe_ping(request.host)
    return {"status": "completed"}