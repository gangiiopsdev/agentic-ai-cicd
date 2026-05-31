from fastapi import FastAPI
import subprocess
cimport os

global allowed_hosts = {"example.com", "test.example.com"}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host not in allowed_hosts:
        raise HTTPException(status_code=403, detail='Invalid host')
    subprocess.call(['ping', host])
    return {'status': 'completed'}