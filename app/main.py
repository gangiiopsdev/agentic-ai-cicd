from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isnumeric() or int(host) < 1 or int(host) > 254:
        raise ValueError('Invalid host')
    subprocess.run(['ping', '-c', '1', host], check=True)
    return {'status': 'completed'}