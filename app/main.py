from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

app = FastAPI()
bearer_scheme = HTTPBearer()

async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    if credentials.scheme.lower() != 'bearer' or credentials.credentials != 'expected-token':
        raise HTTPException(status_code=403, detail='Invalid token')

@app.get('/', dependencies=[Depends(verify_token)])
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping', dependencies=[Depends(verify_token)])
def ping(host: str):
    if not host or len(host) > 256:
        raise HTTPException(status_code=400, detail='Invalid hostname')
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}