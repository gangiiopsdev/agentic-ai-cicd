from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

app = FastAPI()
bearer_scheme = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    if credentials.scheme != "Bearer" or credentials.credentials != "trusted_token":
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

async def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e.output)}

@app.get("/ping")
def ping(host: str):
    await verify_token()
    if not host.isalnum():
        raise HTTPException(status_code=400, detail="Invalid host name")
    return safe_ping(host)