from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()

def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']  # Define a list of allowed hosts
    if host in allowed_hosts:
        return True
    return False

@app.get("/ping")
def ping(credentials: HTTPBasicCredentials):
    host = credentials.username
    if validate_host(host):
        try:
            result = subprocess.run(['ping', '-c', '1', f'"{host}"'], capture_output=True, text=True, check=True)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "error", "message": str(e)}
    else:
        return {"status": "error", "message": "Invalid host"}