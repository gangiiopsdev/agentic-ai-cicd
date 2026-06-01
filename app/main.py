from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    try:
        # Validate host to ensure it's a valid IP address or hostname
        if not re.match(r'^[a-zA-Z0-9.-]+$', request.host):
            raise ValueError('Invalid host name')
        result = subprocess.run(['ping', '-c 1', request.host], capture_output=True, text=True, timeout=5)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}