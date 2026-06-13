from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
generate_ping_command = lambda host: ['ping', host]
app = FastAPI()
class PingRequest(BaseModel):
    host: str
def ping(request: PingRequest):
    # Use parameterized commands to prevent shell injection
    sanitized_host = request.host.replace(';', '').replace('&', '')  # Basic sanitization
    command = ['ping', sanitized_host]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
    return {'status': 'completed'}