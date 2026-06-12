from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        raise Exception('Unsafe host provided')
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}