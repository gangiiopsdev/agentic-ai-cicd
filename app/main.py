from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        subprocess.run(['ping', host], check=True)
        return {"status": "completed"}
    else:
        raise ValueError("Unsafe host")