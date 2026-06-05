from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    safe_hosts = ['127.0.0.1', '::1']  # Add more safe hosts as needed
    return host in safe_hosts

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        subprocess.call(['ping', host])
    else:
        return {'status': 'error', 'message': 'Invalid host'}

    return {'status': 'completed'}