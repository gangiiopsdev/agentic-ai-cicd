from fastapi import FastAPI
import subprocess
def validate_host(host):
    if not host.isalnum() or len(host) > 100:
        raise ValueError('Invalid host name')

app = FastAPI()

@app.get('/ping')
def ping(host: str):