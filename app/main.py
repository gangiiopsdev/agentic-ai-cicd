from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    args = ['ping'] + shlex.split(host)
    subprocess.run(args, check=True)
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    return safe_ping(host)