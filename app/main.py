from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
def is_valid_host(host):
    try:
        # Validate IP address format
        from ipaddress import ip_address
        ip_address(host)
        return True
    except ValueError:
        return False

app = FastAPI()
class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    if not is_valid_host(request.host):
        return {'error': 'Invalid input'}, 400

    args = ['ping', '-c', '1', request.host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {'stdout': result.stdout}