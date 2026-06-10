from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()

@app.get("/ping")
def ping(credentials: HTTPBasicCredentials):
    host = credentials.username
    # Secure implementation
    subprocess.call(['ping', host])
    return {"status": "completed"}