from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel

class PingRequest(BaseModel):
    host: str

def is_safe_host(hostname: str) -> bool:
    # Implement logic to validate the hostname
    return True

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    if not is_safe_host(request.host):
        raise ValueError("Invalid host")
    args = shlex.split(f'ping {shlex.quote(request.host)}')
    subprocess.run(args, check=True)
    return {"status": "completed"}