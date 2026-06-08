from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic_settings import BaseSettings

app = FastAPI()

security = HTTPBasic()

class Settings(BaseSettings):
    admin_username: str = 'admin'
    admin_password: str = 'secret'

settings = Settings()

async def verify_password(username: str, password: str):
    return username == settings.admin_username and password == settings.admin_password

@app.get("/ping")
def ping_route(credentials: HTTPBasicCredentials = Depends(security)):
    host = credentials.username  # Assuming the host is the username for simplicity
    try:
        output = subprocess.run(['/usr/bin/ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': output.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}