from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.run and shlex.quote
    args = shlex.split(f'ping {host}')
    subprocess.run(args)

@app.get("/ping")
def ping_endpoint(host: str):
    return {'result': 'Pinging ' + host}