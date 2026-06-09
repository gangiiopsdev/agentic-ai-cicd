from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.status import HTTP_401_UNAUTHORIZED

security = HTTPBasic()

async def authenticate(credentials: HTTPBasicCredentials):
    correct_username = 'admin'
    correct_password = 'secret'
    if credentials.username == correct_username and credentials.password == correct_password:
        return credentials.username
    else:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail='Incorrect email or password',
            headers={'WWW-Authenticate': 'Basic realm="API"'},
        )

@app.get("/ping")
def ping(host: str, username: str = Depends(authenticate)):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": f'Status Code: {result.returncode}, Output: {result.stdout}'}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}