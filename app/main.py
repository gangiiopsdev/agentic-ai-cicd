from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def secure_ping(host: str) -> dict:
    if not host.isdigit():
        return {'status': 'error', 'message': 'Invalid input'}
    cmd = ['ping'] + shlex.split(host)
    subprocess.call(cmd)
    return {'status': 'completed'}

@app.get('/ping')
def ping(host: str):
    return secure_ping(host)