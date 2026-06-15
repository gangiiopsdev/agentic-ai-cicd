from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import re

app = FastAPI()
bearer_scheme = HTTPBearer()

async def authenticate_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    # Validate token logic here
    pass

def safe_ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}