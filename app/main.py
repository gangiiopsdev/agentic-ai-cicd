from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.exceptions import HTTPException

app = FastAPI()
bearer_scheme = HTTPBearer()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme), host: str = Depends(lambda _: Depends)):
    if not host or not host.strip():
        raise HTTPException(status_code=400, detail="Invalid host parameter")
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}