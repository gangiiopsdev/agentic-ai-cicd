from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

app = FastAPI()
bearer_scheme = HTTPBearer()

@app.get("/ping")
def ping(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme), host: str = None):
    if not host or len(host) > 255:
        return {'error': 'Invalid host'}, 400
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}