from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
import shlex
class PingRequest(BaseModel):
    host: str
def sanitize_host(host):
    return ''.join(e for e in host if e.isalnum() or e in ('.', ':'))
app = FastAPI()
@app.post("/ping")
def ping(request: PingRequest):
    try:
        # Validate and sanitize the input to avoid command injection
        sanitized_host = sanitize_host(request.host)
        args = ['ping', shlex.quote(sanitized_host)]
        result = subprocess.run(args, check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}