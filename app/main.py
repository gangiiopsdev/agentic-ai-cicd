from fastapi import FastAPI
import subprocess

app = FastAPI()

def get_safe_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Define a whitelist of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    get_safe_host(host)
    subprocess.run(['ping'], check=True, args=[host])
    return {"status": "completed"}