from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import base64
def safe_ping(host):
    return ['ping', host]

app = FastAPI()
bearer_scheme = HTTPBearer()

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.check_output(safe_ping(host), stderr=subprocess.STDOUT, universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}