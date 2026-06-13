from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    allowed_hosts = ['localhost', '127.0.0.1']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.call(['ping', host])
    return {'status': 'completed'}