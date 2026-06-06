from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        subprocess.call(['ping', host])
    else:
        raise ValueError('Unauthorized host')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}