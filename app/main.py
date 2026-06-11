from fastapi import FastAPI
import subprocess

async def validate_host(host):
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    subprocess.call(['ping', '-c', '4', host])