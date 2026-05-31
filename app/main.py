from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()

def safe_ping(host: str):
    # Whitelisted hosts or IP ranges
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Invalid host'}

    try:
        output = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(credentials: HTTPBasicCredentials = Depends(security)):
    # Ensure only authorized users can perform this action
    correct_username = "admin"
    correct_password = "secret"
    username = credentials.username
    password = credentials.password
    if username != correct_username or password != correct_password:
        return {'status': 'failed', 'error': 'Invalid credentials'}
    return safe_ping(credentials.username)