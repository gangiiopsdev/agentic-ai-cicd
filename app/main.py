from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using a whitelist for allowed hosts
    safe_hosts = ['127.0.0.1', 'localhost']
    if host in safe_hosts:
        subprocess.call(['ping', host])

@app.get('/ping')
def ping_endpoint(host: str):
    return {'status': ping(host)}