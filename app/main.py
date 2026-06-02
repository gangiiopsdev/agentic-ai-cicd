from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['localhost', '127.0.0.1']
    return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        subprocess.call(['ping', host], shell=False)
    else:
        raise ValueError('Invalid host')
    return {"status": "completed"}