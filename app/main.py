from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.context import CryptContext

app = FastAPI()
security = HTTPBasic()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def authenticate_user(username: str, password: str):
    return pwd_context.verify(password, "hashed_password")

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "failed", "error": "Invalid host"}
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}