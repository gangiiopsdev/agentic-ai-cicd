from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

app = FastAPI()
bearer_scheme = HTTPBearer()

async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    if credentials.scheme.lower() != 'bearer':
        raise HTTPException(status_code=403, detail='Invalid authentication scheme')
    # Add token verification logic here

@app.get("/ping")
def ping(host: str):
    # Ensure the host parameter is validated and sanitized before using it in subprocess
    if not is_valid_host(host):
        raise HTTPException(status_code=400, detail='Invalid host parameter')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "result": result.stdout}

def is_valid_host(host: str) -> bool:
    # Implement validation logic for the host parameter
    import re
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return bool(pattern.match(host))