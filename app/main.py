from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

app = FastAPI()
bearer_scheme = HTTPBearer()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum() or len(host) > 255:
        return {"status": "error", "message": "Invalid host name"}
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}