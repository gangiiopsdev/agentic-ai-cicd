from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    if not host or not host.strip():
        raise ValueError('Invalid input')
    return shlex.quote(host)

@app.get('/ping')
async def ping(host: str):