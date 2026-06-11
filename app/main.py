from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel

app = FastAPI()
bearer_scheme = HTTPBearer()

class TokenData(BaseModel):
    username: str = None

def secure_ping(host: str):
    # Secure implementation with input validation and escaping
    if not host.isalnum():
        raise ValueError('Invalid host name')
    try:
        output = subprocess.check_output(['ping', '-c 1', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}

@app.get("/ping")
def ping(host: str, credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    return secure_ping(host)