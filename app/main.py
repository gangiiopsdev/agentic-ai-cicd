from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi import Depends, HTTPException, status

app = FastAPI()
bearer_scheme = HTTPBearer()

class HostRequest(BaseModel):
    host: str

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.post("/ping")
def ping(host_request: HostRequest, credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    if credentials.scheme != "Bearer" or not credentials.credentials:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid authentication credentials")
    subprocess.call(['ping', host_request.host])
    return {"status": "completed"}