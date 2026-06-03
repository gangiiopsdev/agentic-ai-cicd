from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

def validate_host(host: str) -> bool:
    # Implement validation logic here, e.g., check if the host is within a whitelist
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts

app = FastAPI()
class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    if not validate_host(request.host):
        return {'status': 'failed', 'error': 'Invalid host'}

    try:
        # Sanitize the input by using subprocess.run with shell=False and executable specified
        result = subprocess.run(['ping', request.host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}