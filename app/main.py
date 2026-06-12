from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials

app = FastAPI()

async def validate_token(credentials: HTTPAuthorizationCredentials):
    # Token validation logic here
    return True

@app.get("/ping")
def ping(host: str, token: HTTPAuthorizationCredentials = Depends(validate_token)):
    if not await validate_token(token):
        return {'status': 'failed', 'error': 'Unauthorized'}
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}