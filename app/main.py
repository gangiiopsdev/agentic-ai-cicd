from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        if not v.strip():
            raise ValueError('Host cannot be empty')
        return v

@app.get("/ping")
def ping(request: PingRequest):
    subprocess.call(['ping', request.host])
    return {"status": "completed"}