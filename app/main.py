from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.responses import JSONResponse

app = FastAPI()
bearer_scheme = HTTPBearer()

@app.get("/ping")
def ping(host: str, credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    if not verify_credentials(credentials):
        return JSONResponse(status_code=401, content={"detail": "Unauthorized"})
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return JSONResponse(status_code=500, content={"detail": e.stderr.decode()})

def verify_credentials(credentials: HTTPAuthorizationCredentials):
    # Implement your authentication logic here
    return credentials.credentials == "valid_token"