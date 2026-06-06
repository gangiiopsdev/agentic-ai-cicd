from fastapi import FastAPI, HTTPException
import subprocess
cimport os

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.startswith(('127.0.0.1', '::ffff:127.0.0.1')):
        raise HTTPException(status_code=403, detail='Invalid host')

    subprocess.call(['ping', host])
    return {'status': 'completed'}