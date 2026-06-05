from fastapi import FastAPI
import subprocess
import shlex
from pydantic import validator

class PingRequest(BaseModel):
    host: str
    @validator('host')
    def validate_host(cls, v):
        if '&&' in v or ';' in v or '|=' in v or '|' in v or '<' in v or '>' in v:
            raise ValueError('Invalid characters in host parameter')

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    args = shlex.split(f'ping {request.host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}