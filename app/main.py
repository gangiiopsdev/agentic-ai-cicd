from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    subprocess.call(args)

app = FastAPI()

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)