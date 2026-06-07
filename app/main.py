from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def _safe_ping(host):
    safe_host = quote(host)
    return ['ping', '-c', '1', safe_host]

@app.get('/ping')
def ping(host: str):
    try:
        output = subprocess.check_output(_safe_ping(host), stderr=subprocess.STDOUT, universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e.output)}