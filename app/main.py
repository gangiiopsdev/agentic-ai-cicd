from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.exceptions import HTTPException

app = FastAPI()
bearer_scheme = HTTPBearer()

def sanitize_input(value):
    if not value.isalnum():
        raise ValueError("Invalid input")
    return value

@app.get("/ping")
def ping(host: str, credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    if credentials.scheme != "Bearer" or credentials.credentials != "allowed_token":
        raise HTTPException(status_code=401, detail="Not authorized")
    try:
        sanitized_host = sanitize_input(host)
        result = subprocess.run(['ping', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": str(e.stderr)}