from fastapi import FastAPI
import subprocess
import re
cimport = 'ping {{}}'

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input
    if not re.match('^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname or IP address')
    # Safe implementation
    subprocess.run([cimport.format(host)], shell=False, check=True)
    return {'status': 'completed'}