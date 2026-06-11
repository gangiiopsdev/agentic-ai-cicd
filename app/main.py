from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str
app = FastAPI()
def safe_ping(host):
    if not is_safe_host(host):
        raise ValueError("Unsafe host")
    return subprocess.run(['ping', host], capture_output=True, text=True, check=True)
@app.get("/ping")
def ping(request: PingRequest):  # Use Pydantic model for input validation
    try:
        output = safe_ping(request.host)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}
def is_safe_host(host):
    # Implement your logic to check if the host is safe
    return True