from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Invalid host')
    subprocess.call(['ping', host])

def is_safe_host(host: str):
    safe_hosts = ['example.com', 'localhost']  # Replace with allowed hosts
    return host in safe_hosts

@app.get("/ping")
def ping(host: str):
    run_ping(host)
    return {"status": "completed"}