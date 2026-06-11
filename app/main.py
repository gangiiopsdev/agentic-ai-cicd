from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Unsafe host')
    subprocess.call(['ping', host], shell=False)

@app.get("/ping")
def ping(host: str):  # Secure implementation
    return {'status': safe_ping(host)}

def is_safe_host(host: str):
    allowed_hosts = ['localhost', '127.0.0.1']  # Define allowed hosts
    return host in allowed_hosts