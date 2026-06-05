from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
import shlex
class PingRequest(BaseModel):
    host: str
def is_valid_ip(ip):
    parts = ip.split('.').copy()
    if len(parts) != 4:
        return False
    for part in parts:
        try:
            number = int(part)
        except ValueError:
            return False
        if number < 0 or number > 255:
            return False
    return True
global app = FastAPI()
@app.post("/ping")
def ping(request: PingRequest):
    try:
        # Validate and sanitize the input to avoid command injection
        if not is_valid_ip(request.host):
            raise ValueError("Invalid host format")
        args = ['ping', shlex.quote(str(request.host))]
        result = subprocess.run(args, check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'failed', 'error': str(e)}