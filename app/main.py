from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.status import HTTP_401_UNAUTHORIZED

app = FastAPI()
security = HTTPBasic()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(credentials: HTTPBasicCredentials = Depends(security)):
    host = credentials.username  # Assuming host is provided in the username field for simplicity
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}