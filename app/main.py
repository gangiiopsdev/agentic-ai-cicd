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
        # Use subprocess.run instead of subprocess.call and ensure safe input
        args = ['ping', '-c', '1', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")