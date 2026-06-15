from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if '&&' in v or ';' in v or '|' in v:
            raise ValueError('Invalid characters in host name')
        return v

@app.get("/ping")
def ping(request: PingRequest):
    output = execute_ping(request.host)
    return {"status": "completed", "output": output}

def execute_ping(host: str):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout