from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    safe_hosts = ['127.0.0.1', '::1']  # Define a list of allowed hosts
    return host in safe_hosts

@app.get="/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'error', 'message': 'Host is not allowed'}
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}