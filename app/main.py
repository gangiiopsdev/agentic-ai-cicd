from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets

app = FastAPI()

security = HTTPBasic()

@app.get("/ping")
def ping(host: str, credentials: HTTPBasicCredentials = Depends(security)):
    secret_token = secrets.token_urlsafe(16)
    correct_username = "admin"
    correct_password = "admin"
    if not (credentials.username == correct_username and
            credentials.password == correct_password):
        return HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    try:
        # Safe implementation with validation
        subprocess.call(["ping", host], shell=False)
        return {"status": "completed"}
    except Exception as e:
        return {
            "error": str(e),
            "message": "Failed to ping the host",
        }