from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()

@app.get("/ping")
def ping(credentials: HTTPBasicCredentials = Depends(security)):
    # Secure implementation with input validation and sanitization
    allowed_hosts = ['example.com', 'test.example.com']  # Define a whitelist of allowed hosts
    host = credentials.username
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Unauthorized access'}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}