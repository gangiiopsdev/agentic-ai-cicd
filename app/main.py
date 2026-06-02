from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

def safe_ping(host):
    if not is_safe_host(host):
        raise ValueError('Unsafe host provided')
    return f'ping -c 1 {host}'

def is_safe_host(host):
    # Implement logic to validate the host
    return host == 'safehost'

app = FastAPI()
class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    try:
        result = subprocess.run(safe_ping(request.host).split(), shell=False, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}