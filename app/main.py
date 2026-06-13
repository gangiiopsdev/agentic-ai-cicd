from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.status import HTTP_401_UNAUTHORIZED

app = FastAPI()
security = HTTPBasic()

async def verify_credentials(credentials: HTTPBasicCredentials):
    correct_username = credentials.username == "admin"
    correct_password = credentials.password == "secret"
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials

async def get_current_active_user(credentials: HTTPBasicCredentials = Depends(verify_credentials)):
    return credentials

@app.get("/ping")
def ping(host: str, current_user: HTTPBasicCredentials = Depends(get_current_active_user)):
    is_success, result = safe_ping(host)
    if is_success:
        return {'status': 'completed', 'output': result}
    else:
        return {'status': 'failed', 'error': result}