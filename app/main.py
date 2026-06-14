from fastapi import FastAPI
import subprocess
import shlex
def secure_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::ffff:127.0.0.1']
    if host in allowed_hosts:
        safe_host = shlex.quote(host)
        subprocess.run(['ping', safe_host], shell=False, check=True)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    secure_ping(host)
    return {'status': 'completed'}