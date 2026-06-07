from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.status import HTTP_401_UNAUTHORIZED

app = FastAPI()
security = HTTPBasic()

async def authenticate_user(credentials: HTTPBasicCredentials):
    correct_username = "fake"
    correct_password = "fake"
    return credentials.username == correct_username and credentials.password == correct_password

@app.get("/ping")
def ping(host: str, credentials: HTTPBasicCredentials = Depends(authenticate_user)):
    try:
        # Use a full path for the subprocess call to mitigate command injection risks
        output = subprocess.check_output(['/usr/bin/ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'result': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}