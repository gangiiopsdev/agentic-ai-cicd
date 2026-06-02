from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
import re

class PingRequest(BaseModel):
    host: str

def validate_host(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host format')
    return host

app = FastAPI()

@app.post("/ping")
def ping(request: PingRequest):
    try:
        validated_host = validate_host(request.host)
        args = ['ping', *shlex.split(validated_host)]
        result = subprocess.run(args, check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'failed', 'error': str(e)}