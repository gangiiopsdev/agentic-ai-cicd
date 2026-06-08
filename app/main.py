from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if host.isnumeric():
        return subprocess.call(['ping', host], shell=False)
    else:
        raise ValueError('Invalid host')

@app.get="/ping")
def ping(host: str):
    return {'status': safe_ping(host)}