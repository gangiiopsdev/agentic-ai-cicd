from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        return {'error': 'Invalid hostname'}
    subprocess.call(['ping'] + shlex.split(host))

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)