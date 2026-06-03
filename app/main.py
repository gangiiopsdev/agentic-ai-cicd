from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel

security = HTTPBearer()

class Host(BaseModel):
    host: str

def safe_ping(host: str) -> str:
    args = ['ping', '-c', '1', host]  # Limit the number of pings and use defaults to mitigate injection risks
    result = subprocess.run(args, capture_output=True, text=True, shell=False)
    return result.stdout

def check_host_validity(host: str) -> bool:
    valid_hosts = ['example.com', 'localhost']  # Example list of allowed hosts
    return host in valid_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: Host = Depends(security)):
    if not check_host_validity(host.host):
        raise HTTPException(status_code=403, detail="Invalid host")
    output = safe_ping(host.host)
    return {"status": "completed", "output": output}