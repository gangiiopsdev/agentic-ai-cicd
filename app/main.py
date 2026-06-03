from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import Depends
import shlex

app = FastAPI()

async def verify_auth(credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
    if credentials.scheme != "Bearer":
        raise HTTPException(status_code=403, detail="Invalid authentication scheme")
    return credentials.credentials

@app.get('/ping')
def ping(host: str, token: str = Depends(verify_auth)):
    try:
        output = subprocess.check_output(shlex.split(f'ping {host}'), stderr=subprocess.STDOUT, universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.output}