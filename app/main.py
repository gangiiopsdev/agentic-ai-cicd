from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str) -> bool:
    return not host.strip() or '@' in host

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if safe_ping(host):
        raise ValueError('Invalid host parameter')
    cmd = ['ping', shlex.quote(host)]
    output = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': output.stdout}