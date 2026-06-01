from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

app = FastAPI()
bearer_scheme = HTTPBearer()

@app.get("/ping")
def ping(host: str, credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    # Sanitize input and validate permissions
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    if host not in allowed_hosts:
        return {'error': 'Unauthorized host'}, 403
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}