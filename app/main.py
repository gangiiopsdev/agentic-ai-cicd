from fastapi import FastAPI
import subprocess
def is_safe_host(host):
    safe_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    return host in safe_hosts

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if is_safe_host(host):
        subprocess.call(['ping', host])  # Remove '--' to fix the issue
        return {'status': 'completed'}
    else:
        return {'status': 'denied'}, 403