from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import Depends

app = FastAPI()

async def verify_access(credentials: HTTPAuthorizationCredentials = Depends()):
    if credentials.scheme != "Bearer":
        raise HTTPException(status_code=403, detail="Invalid authentication scheme")
    if credentials.credentials != "secret_token":
        raise HTTPException(status_code=401, detail="Invalid token")

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str, credentials: HTTPAuthorizationCredentials = Depends(verify_access)):
    # Safer implementation with input validation and authorization
    if host not in ["127.0.0.1", "localhost"]:
        raise HTTPException(status_code=403, detail="Invalid host")
    subprocess.call(["ping", host])
    return {"status": "completed"}