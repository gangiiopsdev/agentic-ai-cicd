from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

app = FastAPI()
bearer_scheme = HTTPBearer()

@app.get("/ping")
def ping(host: str, credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    # Validate host input to prevent command injection
    if not host.isdigit():
        raise ValueError("Invalid host")
    subprocess.call(['ping', host])
    return {"status": "completed"}