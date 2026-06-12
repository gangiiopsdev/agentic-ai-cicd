from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()

def verify_password(username: str, password: str):
    return username == 'admin' and password == 'secret'

@app.get("/ping")
def ping(credentials: HTTPBasicCredentials = Depends(security)):
    username = credentials.username
    password = credentials.password
    if not verify_password(username, password):
        return {'status': 'failed', 'error': 'Invalid credentials'}
    host = credentials.username  # Assuming username is the host to ping
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}