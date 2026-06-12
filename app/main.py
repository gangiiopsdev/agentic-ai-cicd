from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
dependency = HTTPBearer()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': e.output.decode()}