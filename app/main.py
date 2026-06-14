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
        output = subprocess.check_output(["ping", request.host], stderr=subprocess.STDOUT, shell=False)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}
    except ValueError as ve:
        return {"status": "failed", "error": str(ve)}