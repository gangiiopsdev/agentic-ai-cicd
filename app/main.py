from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()

def safe_ping(host):
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    try:
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(credentials: HTTPBasicCredentials = Depends(security)):
    return {"message": safe_ping(credentials.username)}