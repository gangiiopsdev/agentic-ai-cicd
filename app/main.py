from fastapi import FastAPI
import subprocess
def is_safe_host(host):
    safe_hosts = ['127.0.0.1', '::1']
    return host in safe_hosts

app = FastAPI()

@app.get('/ping')
def ping(host: str):