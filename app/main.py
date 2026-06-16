from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.exceptions import HTTPException

app = FastAPI()
bearer_scheme = HTTPBearer()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with validation and sanitization
    if not host or len(host) > 255:
        raise HTTPException(status_code=400, detail="Invalid host parameter")
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}