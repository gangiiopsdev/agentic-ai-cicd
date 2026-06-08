from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import secrets

def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Replace with your own validation logic
    if host not in allowed_hosts or len(host) > 256:
        return False
    return True

def safe_ping(host):
    try:
        result = subprocess.run(['ping', '-c', '1'], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}

app = FastAPI()
bearer_scheme = HTTPBearer()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    return safe_ping(host)