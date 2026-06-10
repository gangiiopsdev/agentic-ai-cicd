from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.context import CryptContext

app = FastAPI()

security = HTTPBasic()
crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and sanitization
    if not host.isalnum():
        raise Exception("Invalid hostname")
    safe_host = subprocess.list2cmdline([host])  # Sanitize the input
    result = subprocess.run(['ping', safe_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}