from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

app = FastAPI()
bearer_scheme = HTTPBearer()

@app.get("/ping")
def ping(host: str, credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    # Ensure only authorized users can perform this action
    if credentials.scheme != "Bearer" or credentials.credentials != "secret_token":
        return {"status": "unauthorized"}
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}