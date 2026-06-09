from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with shell=False and validate input
    if host.startswith('localhost.') or host == '127.0.0.1':
        subprocess.call(['ping', host], shell=False)
    else:
        raise ValueError('Invalid host')