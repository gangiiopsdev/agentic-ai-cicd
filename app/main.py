from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

def safe_ping(host):
    if not is_safe_host(host):
        raise ValueError('Unsafe host provided')
    return 'ping' + ' -c' + ' 1' + ' ' + host

def is_safe_host(host):
    # Implement more robust logic to validate the host
    allowed_hosts = ['safehost', 'another_safe_host']
    return host in allowed_hosts

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def execute_ping_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.post('/ping')
def ping(request: PingRequest):
    safe_command = safe_ping(request.host)
    return execute_ping_command(safe_command)