from fastapi import FastAPI
import subprocess
import shlex
cimport = ('ping', 'localhost')

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if host not in cimport:
        return {'error': 'Invalid host'}
    cmd = ['ping'] + shlex.split(host)
    subprocess.run(cmd, check=True)
    return {'status': 'completed'}