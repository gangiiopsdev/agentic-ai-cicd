from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

app = FastAPI()
bearer_scheme = HTTPBearer()

def safe_ping(host):
    allowed_hosts = ['localhost']
    if host in allowed_hosts:
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': str(e)}
    else:
        return {'status': 'error', 'message': 'Invalid host'}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)