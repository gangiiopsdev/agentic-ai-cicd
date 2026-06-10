from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

app = FastAPI()
bearer_scheme = HTTPBearer()

@app.get("/ping")
def ping(host: str):
    # Validate input to avoid command injection
    if not host.isalnum():
        return {'error': 'Invalid host'}, 400
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {
        "status": "completed",
        "output": result.stdout,
        "error": result.stderr if result.returncode != 0 else None
    }