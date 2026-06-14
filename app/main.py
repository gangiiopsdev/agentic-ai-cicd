from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi import Depends, HTTPException, status
from shlex import quote as shell_quote

app = FastAPI()
bearer_scheme = HTTPBearer()

async def verify_token(token: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    # Add token verification logic here
    return True

def is_valid_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Add valid hosts here
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str, token: HTTPAuthorizationCredentials = Depends(verify_token)):
    if not is_valid_host(host):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Invalid host')
    result = subprocess.run(['ping', '-c', '1', shell_quote(host)], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}