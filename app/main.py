from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

app = FastAPI()
bearer_scheme = HTTPBearer()

async def validate_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    # Add token validation logic here
    return credentials.credentials

@app.get("/ping")
def ping(host: str, token: str = Depends(validate_token)):
    try:
        result = subprocess.run(["ping", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}