from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.context import CryptContext

app = FastAPI()

http_basic = HTTPBasic()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@app.get("/ping")
def ping(credentials: HTTPBasicCredentials = Depends(http_basic)):
    host = credentials.username
    if pwd_context.verify(credentials.password, "expected_password_hash"):
        args = ['ping', '-c', '1', host]  # Limit the number of pings to avoid abuse
        subprocess.call(args)
        return {"status": "completed"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")