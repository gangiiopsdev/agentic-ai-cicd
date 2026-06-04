from fastapi import FastAPI
import subprocess
cimport os

cdef ping(host: str):
    cdef bytes host_bytes = host.encode('utf-8')
    if host in ['localhost', '127.0.0.1']:
        command = b'ping' + os.fsencode(' ') + host_bytes
        subprocess.call(command, shell=False)
        return {'status': 'completed'}
    else:
        return {'error': 'Unauthorized access attempt'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_fastapi(host: str):
    return ping(host)