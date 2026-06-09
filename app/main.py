from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    allowed_hosts = ['127.0.0.1', 'localhost']  # Define allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

@app.get("/ping")
def ping(host: str):
    sanitize_host(host)
    subprocess.call(['ping', host])
    return {"status": "completed"}