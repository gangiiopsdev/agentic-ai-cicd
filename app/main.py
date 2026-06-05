from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    safe_hosts = ['127.0.0.1', '::1']
    return host in safe_hosts

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Invalid host')
    subprocess.call(['ping', host])
    return {'status': 'completed'}