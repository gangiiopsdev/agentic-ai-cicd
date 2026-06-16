from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.exceptions import HTTPException
def validate_host(host):
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
generate_ping_command = lambda host: f'ping {host}'
app = FastAPI()
bearer_scheme = HTTPBearer()
@app.get('/ping')
def ping(authorization: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    try:
        validate_host(authorization.credentials)
        subprocess.run(generate_ping_command(authorization.credentials), shell=False, check=True)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}