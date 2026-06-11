from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    allowed_hosts = ['localhost', '127.0.0.1']
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    # Secure implementation using shell=False and a list of arguments
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}