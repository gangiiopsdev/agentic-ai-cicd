from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e == '.' or e == '-').strip()

app = FastAPI()
class PingRequest(BaseModel):
    host: str

def is_valid_host(host):
    valid_hosts = ['example.com', 'test.com']  # Example whitelist
    return host in valid_hosts

@app.post("/ping")
def ping(request: PingRequest):
    sanitized_host = sanitize_input(request.host)
    if not is_valid_host(sanitized_host):
        return {'status': 'error', 'output': 'Invalid host'}
    try:
        result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}