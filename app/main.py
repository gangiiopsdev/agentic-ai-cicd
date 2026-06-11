from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

app = FastAPI()
bearer_scheme = HTTPBearer()

async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    if credentials.scheme != 'Bearer' or credentials.credentials != 'your_secret_token':
        raise HTTPException(status_code=401, detail='Invalid authentication credentials')

@app.post('/ping')
def ping_handler(host: str, token: HTTPAuthorizationCredentials = Depends(verify_token)):
    # Secure implementation with input validation and authentication
    if not host or not isinstance(host, str) or len(host) > 255:
        raise HTTPException(status_code=400, detail='Invalid host parameter')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'result': result.stdout}