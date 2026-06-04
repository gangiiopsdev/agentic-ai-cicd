from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

app = FastAPI()
security = HTTPBearer()

class HostRequest(BaseModel):
    host: str

async def validate_host(host: str):
    # Implement validation logic here (e.g., allowed hosts list)
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise HTTPException(status_code=403, detail="Unauthorized host")

@app.get("/ping", dependencies=[Depends(validate_host)])
def ping_route(request: HostRequest):
    args = ['ping', '-c', '4', request.host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'output': result.stdout}