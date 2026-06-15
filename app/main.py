from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class PingResponse(BaseModel):
    status: str

def is_valid_host(host):
    return host.replace('.', '').isalnum()

app = FastAPI()

@app.get("/ping")
def ping(host: str):  # Secure implementation
    if not is_valid_host(host):
        raise ValueError("Invalid host name")
    safe_host = subprocess.quote(host)
    result = subprocess.run(["ping", "-c", "1", safe_host], capture_output=True, text=True)
    return PingResponse(status=result.stdout)