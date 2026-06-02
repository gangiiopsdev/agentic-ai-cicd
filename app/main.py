from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str
def validate_host(host):
    if not host or not host.strip():
        raise ValueError('Invalid host')
    return host

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    try:
        validated_host = validate_host(request.host)
        output = subprocess.run(['ping', validated_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'failed', 'error': str(e)}