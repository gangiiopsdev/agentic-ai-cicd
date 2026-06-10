from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class PingRequest(BaseModel):
    host: str

def is_safe_host(host):
    # Implement a function to validate and sanitize the host
    return host.replace(' ', '_').replace('.', '_')

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    safe_host = is_safe_host(request.host)
    if not safe_host:
        raise ValueError("Invalid host")
    subprocess.run(['ping', safe_host], check=True)
    return {'status': 'completed'}