from fastapi import FastAPI
import subprocess
from fastapi.exceptions import HTTPException
global allowed_hosts
allowed_hosts = ['127.0.0.1', '::1']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host not in allowed_hosts:
        raise HTTPException(status_code=403, detail='Host not allowed')

    safe_host = subprocess.quote(host)
    subprocess.run(['ping', safe_host], check=True)

    return {'status': 'completed'}