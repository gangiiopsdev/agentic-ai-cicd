from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts

app = FastAPI()
class PingRequest(BaseModel):
    host: str

def execute_ping(host: str) -> str:
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

@app.post("/ping")
def ping(request: PingRequest):
    if not validate_host(request.host):
        return {'status': 'failed', 'error': 'Invalid host'}

    output = execute_ping(request.host)
    return {'status': 'completed', 'output': output}