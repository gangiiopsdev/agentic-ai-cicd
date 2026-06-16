from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.status import HTTP_401_UNAUTHORIZED
globally_safe_hosts = ['safehost1', 'safehost2']

app = FastAPI()
security = HTTPBasic()

@app.get("/ping")
def ping(host: str, credentials: HTTPBasicCredentials = Depends(security)):
    if host not in globally_safe_hosts:
        return "Host is not allowed", HTTP_401_UNAUTHORIZED
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {"status": "completed"}