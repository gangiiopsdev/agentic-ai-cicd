from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host):
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host in allowed_hosts:
        subprocess.run(['ping', host], check=True)
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    secure_ping(host)
    return {"status": "completed"}