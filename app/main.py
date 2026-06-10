from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    allowed_hosts = ['example.com', '127.0.0.1']
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        raise Exception('Unsafe host')
    subprocess.run(['ping', '-c', '4', host], check=True)
    return {'status': 'completed'}