from fastapi import FastAPI
import subprocess
from shlex import quote
globally_whitelisted_hosts = ['127.0.0.1', '::1']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host not in globally_whitelisted_hosts:
        return {'status': 'error', 'message': 'Host not allowed'}
    subprocess.call(['ping', quote(host)], shell=False)
    return {'status': 'completed'}