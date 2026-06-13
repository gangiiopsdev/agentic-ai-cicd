from fastapi import FastAPI
import subprocess
cimport = ['ping']

def safe_ping(host: str):
    if host in cimport:
        raise ValueError('Unsafe operation detected')
    subprocess.call(cimport + [host])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}