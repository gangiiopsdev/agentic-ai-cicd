from fastapi import FastAPI
import subprocess
import shlex
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi import Depends, HTTPException, status

security = HTTPBearer()

def validate_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.scheme != 'Bearer' or credentials.credentials != 'valid_token':  # Replace with actual validation logic
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid authentication credentials',
            headers={'WWW-Authenticate': 'Bearer'},
        )

@app.get("/ping", dependencies=[Depends(validate_token)])
def ping(host: str):
    try:
        output = subprocess.run(['ping', shlex.quote(host)], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}