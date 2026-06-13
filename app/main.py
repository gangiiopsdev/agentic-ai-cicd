from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

app = FastAPI()
bearer_scheme = HTTPBearer()

@app.get("/ping")
def ping(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme), host: str = None):
    if not host or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}