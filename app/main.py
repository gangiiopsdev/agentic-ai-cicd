from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

def validate_host(host):
    allowed_hosts = ['localhost', '127.0.0.1']
    return host in allowed_hosts

class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.post("/ping")
def ping(request: PingRequest):
    if not validate_host(request.host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', '-c', str(1), escape_shell_arg(request.host)], check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
def escape_shell_arg(arg):
    import shlex
    return shlex.quote(arg)