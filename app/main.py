from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

def validate_host(host):
    allowed_hosts = ['example.com', 'test.example.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

app = FastAPI()
class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    try:
        validate_host(request.host)
        output = subprocess.run(['ping', request.host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}
    except ValueError as ve:
        return {"status": "failed", "error": str(ve)}