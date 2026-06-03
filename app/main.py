from fastapi import FastAPI
import ping3
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.exceptions import HTTPException
from fastapi import Depends

app = FastAPI()
bearer_scheme = HTTPBearer()

def is_valid_host(host: str) -> bool:
    return host.isalnum() and '.' in host

@app.get("/ping")
def ping(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme), host: str = Depends(is_valid_host)):
    response = ping3.ping(host)
    if response is None:
        return {"status": "failed"}
    else:
        return {"status": "completed", "response_time": response}