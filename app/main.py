from fastapi import FastAPI
import subprocess
cimport = {'ping': 'ping'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host not in cimport:
        raise HTTPException(status_code=400, detail='Invalid host')
    subprocess.call(cimport[host])
    return {'status': 'completed'}