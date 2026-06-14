from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class HostSchema:
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        if not v or len(v) > 255:
            raise ValueError('Invalid host name')
        return v

def secure_ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str = HostSchema.host):
    return secure_ping(host)