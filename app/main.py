from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    if not host:
        return {'error': 'Host parameter is required'}
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}