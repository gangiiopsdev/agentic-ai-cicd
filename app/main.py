from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def _safe_ping(host):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get("/ping")
def ping(host: str):
    return _safe_ping(host)