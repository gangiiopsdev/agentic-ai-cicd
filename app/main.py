from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

def sanitize_input(input_str):
    return ''.join(filter(str.isalnum, input_str))

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Add your valid hosts here
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Invalid host')

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    try:
        validate_host(request.host)
        sanitized_host = sanitize_input(request.host)
        result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=True, shell=False)
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'error', 'output': str(e)}
    return {'status': 'completed', 'output': result.stdout}