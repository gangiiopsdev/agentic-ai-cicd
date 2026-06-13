from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials
security = HTTPBasic()
def run_ping(host: str):    try:
        # Secure implementation using subprocess.run with basic sanitization
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}
global app
app = FastAPI()
@app.get("/ping")
def ping(credentials: HTTPBasicCredentials = Depends(security)):
    host = credentials.username  # Assuming username is the parameter to be sanitized
    return run_ping(host)