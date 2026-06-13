from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not host.isnumeric() or int(host) > 255:
        raise ValueError('Invalid host value')
    cmd = ['ping', host]
    subprocess.call(cmd)

@app.get="/ping")
def ping(host: str):