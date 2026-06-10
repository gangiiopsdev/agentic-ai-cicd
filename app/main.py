from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

app = FastAPI()
bearer_scheme = HTTPBearer()

def validate_credentials(credentials: HTTPAuthorizationCredentials):
    return credentials.scheme == 'Bearer' and credentials.credentials == 'valid_token'

@app.get('/ping')
def ping(host: str):
    if not validate_credentials(HTTPAuthorizationCredentials(scheme='Bearer', credentials='valid_token')):
        raise Exception('Unauthorized')
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}