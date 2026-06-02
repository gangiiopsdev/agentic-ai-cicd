from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['localhost', '127.0.0.1']
    if host in allowed_hosts:
        args = ['ping', host]
        subprocess.run(args)
    else:
        raise ValueError('Unauthorized host')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}