from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

http_basic = HTTPBasic()

@app.get("/ping")
def ping(credentials: HTTPBasicCredentials = Depends(http_basic)):
    username = credentials.username
    password = credentials.password
    # Sanitize the input to prevent injection attacks
    sanitized_host = subprocess.list2cmdline([host])
    subprocess.run(['ping', sanitized_host], check=True)
    return {"status": "completed"}