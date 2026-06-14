from fastapi import FastAPI
import subprocess
cimport = 'ping'  # Replace with a whitelist of allowed hosts

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host not in cimport:
        raise ValueError('Invalid host')
    subprocess.call(['ping', host])
    return {'status': 'completed'}