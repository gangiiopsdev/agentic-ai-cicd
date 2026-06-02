from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

app = FastAPI()
bearer_scheme = HTTPBearer()

class HostModel(BaseModel):
    host: str

@app.get('/ping')
def ping(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme), host_model: HostModel = Body(...)):
    host = host_model.host
    # Secure implementation
    subprocess.call(['ping', host])
    return {'status': 'completed'}