from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

class PingRequest(BaseModel):
    host: str
    @validator('host')
    def validate_host(cls, v):
        if '&&' in v or ';' in v or '|=' in v or '|' in v or '<' in v or '>' in v:
            raise ValueError('Invalid characters in host parameter')
        return shlex.quote(v)

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    args = ['ping', request.host]
    subprocess.run(args, check=True, shell=False)
    return {'status': 'completed'}