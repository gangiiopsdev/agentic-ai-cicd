from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
import shlex
class PingRequest(BaseModel):
    host: str

def is_valid_host(host):
    return host.isdigit() and len(host) > 3 and not host.startswith('0')

app = FastAPI()

@app.post("/ping")
def ping(request: PingRequest):
    try:
        if not is_valid_host(str(request.host)):
            raise ValueError("Invalid host format")
        args = ['ping', shlex.quote(str(request.host))]
        result = subprocess.run(args, check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'failed', 'error': str(e)}