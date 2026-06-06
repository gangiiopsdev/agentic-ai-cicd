from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    safe_host = ''.join(e for e in host if e.isalnum() or e in ('-', '.', '_'))
    args = shlex.split(f'ping {safe_host}')
    subprocess.call(args)

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}