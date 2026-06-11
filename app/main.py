from fastapi import FastAPI
import subprocess
c from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

app = FastAPI()
bearer_scheme = HTTPBearer()

@app.get('/ping')
def ping(host: str):
    if not host:
        return {'error': 'Host parameter is required'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}