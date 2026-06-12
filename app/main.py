from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def secure_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::ffff:127.0.0.1']
    if host in allowed_hosts:
        safe_host = shlex.quote(host)
        subprocess.call(['ping'], input=safe_host, shell=True)

@app.get('/ping')
def ping(host: str):
    secure_ping(host)
    return {'status': 'completed'}