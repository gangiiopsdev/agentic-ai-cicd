from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::ffff:127.0.0.1']
    if host in allowed_hosts:
        safe_host = subprocess.list2cmdline([host])
        subprocess.call(['ping', safe_host])

@app.get('/ping')
def ping(host: str):
    secure_ping(host)
    return {'status': 'completed'}