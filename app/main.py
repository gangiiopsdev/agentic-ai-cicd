from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f'Ping failed: {result.stderr}')

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}