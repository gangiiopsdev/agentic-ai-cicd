from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials
cred = HTTPBasic()

app = FastAPI()

async def verify(credentials: HTTPBasicCredentials):
    correct_username = credentials.username == "admin"
    correct_password = credentials.password == "admin123"
    if not (correct_username and correct_password):
        raise HTTPException(status_code=401, detail="Incorrect username or password", headers={"WWW-Authenticate": "Basic"})
    return credentials

@app.get('/ping')
def ping(host: str = Depends(verify)):
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}