from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException, status
import shlex

app = FastAPI()

async def verify_token(credentials: HTTPAuthorizationCredentials = Depends()):
    if credentials.scheme != "Bearer":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid authentication scheme",
        )
    # Validate and decode token here
    return credentials.credentials

@app.get("/ping")
def ping(host: str = Depends(verify_token)):
    if not host.startswith('192.168.'):"
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid host",
        )
    try:
        command = ['ping'] + shlex.split(host)
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}