from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    args = ['ping', host]
    subprocess.call(args, shell=False)

app = FastAPI()

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)