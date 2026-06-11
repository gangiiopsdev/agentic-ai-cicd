from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

http_basic = HTTPBasic()

def sanitize_input(input_str):
    if '&&' in input_str or ';' in input_str:
        raise ValueError('Invalid input')
    return input_str

@app.get("/ping")
def ping(credentials: HTTPBasicCredentials = Depends(http_basic)):
    username = credentials.username
    password = credentials.password
    # Sanitize the input to prevent injection attacks
    host = sanitize_input(username)
    sanitized_host = subprocess.list2cmdline([host])
    subprocess.run(['ping', sanitized_host], check=True)
    return {"status": "completed"}