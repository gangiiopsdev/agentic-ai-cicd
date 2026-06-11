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
        # Sanitize the input to prevent command injection using a whitelist approach
        allowed_hosts = ['google.com', 'example.com']
        if host not in allowed_hosts:
            return {'status': 'error', 'message': 'Host not allowed'}
        sanitized_host = subprocess.list2cmdline([host])  # Sanitize the input
        result = subprocess.run(['ping', '--', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}