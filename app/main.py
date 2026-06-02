from fastapi import FastAPI
import subprocess
def is_safe_host(host):
    safe_hosts = ['127.0.0.1', 'localhost']
    return host in safe_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Invalid host")
    # Secure implementation
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}