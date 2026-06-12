from fastapi import FastAPI
import subprocess
class PingRequest(BaseModel):
    host: str
    @validator('host')
    def validate_host(cls, v):
        if not v.isalnum() or len(v) > 255:
            raise ValueError('Invalid host')
        return v
def safe_ping(host):\n    # Use a whitelist of allowed hosts or IP ranges\n    allowed_hosts = ['192.168.0.1', '10.0.0.1']\n    if host not in allowed_hosts:\n        raise ValueError('Host is not allowed')\n    result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)\n    return {'status': 'completed', 'output': result.stdout}\napp = FastAPI()\n@app.post('/ping', response_model=PingRequest)\ndef ping(request: PingRequest):\n    return safe_ping(request.host)