from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid host name')
    return ''.join(e for e in host if e.isalnum())

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    subprocess.call(['ping', sanitized_host], shell=False)
    return {"status": "completed"}