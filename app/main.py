from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        if not all(c.isalnum() or c in ('.', '-', '_') for c in v):
            raise ValueError('Invalid host name')
        return v

@app.post("/ping")
def ping(request: PingRequest):
    safe_host = subprocess.shlex_quote(request.host)
    args = ['ping', safe_host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}