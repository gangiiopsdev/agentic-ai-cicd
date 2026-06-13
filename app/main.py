from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi import Depends, HTTPException, status

app = FastAPI()
bearer_scheme = HTTPBearer()

async def verify_token(token: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    if token.credentials != 'valid_token':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token', headers={'WWW-Authenticate': 'Bearer'})

@app.get('/', dependencies=[Depends(verify_token)])
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get('/ping', dependencies=[Depends(verify_token)])
def ping(host: str):
    if not host.strip().replace('.', '', 3).isdigit():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid hostname')
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}