from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        if not v.strip().startswith(('192.168.', '10.', '172.')):
            raise ValueError('Invalid IP address')
        return v

@app.get("/ping")
def ping(request: PingRequest):
    args = ['ping', request.host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}