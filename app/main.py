from fastapi import FastAPI
import subprocess
def is_safe_host(host):
    safe_hosts = ['127.0.0.1', 'localhost']
    return host in safe_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {"status": "denied", "message": "Host not allowed"}
    # Secure implementation using subprocess.run without shell=True
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}