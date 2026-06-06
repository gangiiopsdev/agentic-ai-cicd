from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

security = HTTPBasic()

async def verify_password(username: str, password: str):
    return username == "admin" and password == "secret"

@app.get("/ping")
def ping_route(credentials: HTTPBasicCredentials = Depends(security)):
    host = credentials.username  # Assuming the host is the username for simplicity
    try:
        output = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': output.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}