from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from typing import Optional

app = FastAPI()
bearer_scheme = HTTPBearer()

@app.get("/ping")
def ping(host: str, credentials: Optional[HTTPAuthorizationCredentials] = Depends(bearer_scheme)):
    try:
        # Sanitize input to prevent command injection
        if not host.isalnum():
            raise ValueError("Invalid host name")
        result = subprocess.run(['ping', host], check=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}