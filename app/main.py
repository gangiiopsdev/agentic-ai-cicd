from fastapi import FastAPI
import ping3
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.exceptions import HTTPException
from fastapi import Depends
import re

app = FastAPI()
bearer_scheme = HTTPBearer()

async def validate_host(host: str) -> bool:
    # Use a regex to validate the host parameter more strictly
    return re.match(r'^([a-zA-Z0-9.-]{1,255}|[a-fA-F0-9:]{1,4}:){1,7}[a-zA-Z0-9.-]{1,255}$', host) is not None

@app.get("/ping")
def ping(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme), host: str = Depends(validate_host)):
    response = ping3.ping(host)
    if response is None:
        return {"status": "failed"}
    else:
        return {"status": "completed", "response_time": response}