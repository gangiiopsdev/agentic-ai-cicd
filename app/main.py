from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.context import CryptContext

app = FastAPI()

security = HTTPBasic()
crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    if not host.isalnum():
        raise Exception("Invalid hostname")
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}