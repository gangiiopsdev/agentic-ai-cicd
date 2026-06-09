from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import secrets

app = FastAPI()
bearer_scheme = HTTPBearer()

@app.get("/ping")
def ping(host: str):
    if not host or len(host) > 256:
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        # Sanitize the input to prevent command injection
        result = subprocess.run(['ping', '--', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}

# Additional security measures
allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
if host not in allowed_hosts:
    return {'status': 'error', 'message': 'Host not allowed'}