from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.exceptions import HTTPException

app = FastAPI()
bearer_scheme = HTTPBearer()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.isdigit():
        raise HTTPException(status_code=400, detail="Invalid host input")
    subprocess.run(f'ping {host}', shell=False, check=True)
    return {"status": "completed"}