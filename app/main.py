from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

def safe_ping(host):
    if not is_safe_host(host):
        raise ValueError('Unsafe host provided')
    return 'ping' + ' -c' + ' 1' + ' ' + host

def is_safe_host(host):
    # Implement logic to validate the host
    return host == 'safehost'

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def execute_ping_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

@app.post("/ping")
def ping(request: PingRequest):
    safe_command = safe_ping(request.host)
    return execute_ping_command(safe_command)