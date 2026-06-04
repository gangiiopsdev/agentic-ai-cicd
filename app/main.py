from fastapi import FastAPI
import subprocess
import shlex
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host')
    def validate_host(cls, v):
        # Simple sanitization example: remove non-alphanumeric characters and specific characters that could be harmful
        return ''.join(e for e in v if e.isalnum() or e in ['.', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])

@app.get("/ping")
def ping(request: PingRequest):
    sanitized_host = request.host
    args = shlex.split(f"ping {sanitized_host}")
    subprocess.call(args, shell=False)

    return {"status": "completed"}