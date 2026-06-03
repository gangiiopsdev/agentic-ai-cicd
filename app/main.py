from fastapi import FastAPI
import subprocess
import shlex
def escape_host(host: str):
    return host.replace(';', '').replace('&', '')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    escaped_host = escape_host(host)
    args = ['ping', '-c', '1', escaped_host]
    subprocess.run(args, check=True, text=True)
    return {'status': 'completed'}