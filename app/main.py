from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel

security = HTTPBearer()

class Host(BaseModel):
    host: str

app = FastAPI()

@app.get("/ping")
def ping(host: Host = Depends(security)):
    args = ['ping', host.host]
    result = subprocess.run(args, capture_output=True, text=True, shell=False)
    return {"status": "completed", "output": result.stdout}