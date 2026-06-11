from fastapi import FastAPI
import subprocess
import shlex
def escape_host(host):
    return ''.join(shlex.quote(c) for c in host if c.isalnum() or c in ['.', '-', '_'])
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    safe_host = escape_host(host)
    subprocess.run(['ping', '-c', '1', safe_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed'}