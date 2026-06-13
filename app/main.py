from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
def sanitize_input(host):
    allowed_hosts = ['example.com', 'test.com']
    return host if host in allowed_hosts else None

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    sanitized_host = sanitize_input(request.host)
    if not sanitized_host:
        return {"status": "failed", "error": "Invalid host"}
    try:
        output = subprocess.check_output(['ping', sanitized_host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode('utf-8')}