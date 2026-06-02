from fastapi import FastAPI
import subprocess
from fastapi import HTTPException

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    allowed_hosts = ['127.0.0.1', 'localhost']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise HTTPException(status_code=403, detail='Unauthorized host')
    try:
        result = subprocess.run(['ping', '-c', '1', host], input=None, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}