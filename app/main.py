from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Fixed implementation
    command = shlex.split(f'ping {host}')
    subprocess.run(command, check=True)
    return {'status': 'completed'}

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)