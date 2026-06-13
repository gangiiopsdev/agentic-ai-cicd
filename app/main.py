from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

app = FastAPI()
bearer_scheme = HTTPBearer()

def safe_ping(host: str):
    try:
        # Validate the host to prevent shell injection
        if not host.replace('.', '').isnumeric():
            raise ValueError("Invalid host")
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

@app.get("/ping")
def ping(host: str, credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    return safe_ping(host)