from fastapi import FastAPI
import subprocess
cimport = ['ping'] + [host]

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    cimport = ['ping', host]
    subprocess.run(cimport, check=True)
    return {'status': 'completed'}