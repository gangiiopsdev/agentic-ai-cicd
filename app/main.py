from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.exceptions import HTTPException
from fastapi import Depends
import ping3

app = FastAPI()
bearer_scheme = HTTPBearer()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme), host: str = Depends(lambda _: Depends)): # Assuming some form of authentication and validation is in place
    if not host.isalnum() or '.' not in host:
        raise HTTPException(status_code=400, detail="Invalid host name")
    response = ping3.ping(host)
    if response is None:
        return {"status": "failed"}
    else:
        return {"status": "completed", "response_time": response}