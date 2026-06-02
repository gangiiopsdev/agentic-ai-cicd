from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
def safe_ping(host: str) -> dict:
    allowed_hosts = ['example.com', 'localhost']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Host is not allowed'}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

class Host(BaseModel):
    host: str

@app.get("/ping")
def ping(host: Host = Depends(Host)) -> dict:
    return safe_ping(host.host)