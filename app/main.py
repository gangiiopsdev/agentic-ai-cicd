from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Implement a whitelist of allowed hosts
    safe_hosts = ['example.com', 'localhost']
    return host in safe_hosts

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise Exception('Unsafe host')
    subprocess.call(['ping', host])
    return {"status": "completed"}