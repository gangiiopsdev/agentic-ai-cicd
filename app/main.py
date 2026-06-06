from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi import Depends, HTTPException

app = FastAPI()
bearer_scheme = HTTPBearer()

async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    if credentials.scheme.lower() != 'bearer' or credentials.credentials != 'secret-token':
        raise HTTPException(status_code=403, detail='Invalid authentication credentials')

@app.get('/', dependencies=[Depends(verify_token)])
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping', dependencies=[Depends(verify_token)])
def ping(host: str):
    try:
        output = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}