from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import secrets

app = FastAPI()
bearer_scheme = HTTPBearer()

async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    if credentials.scheme.lower() != 'bearer' or not verify_password(credentials.credentials):
        raise HTTPException(status_code=403, detail='Invalid authentication token')

def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

@app.get("/ping")
def ping(host: str):
    await verify_token()
    # Sanitize host input to prevent command injection
    if not validate_host(host):
        raise HTTPException(status_code=400, detail='Invalid host')
    return safe_ping(host)

async def verify_password(password: str) -> bool:
    # Placeholder for actual password verification logic
    return True

def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'test.com']  # Replace with actual validation logic
    return host in allowed_hosts