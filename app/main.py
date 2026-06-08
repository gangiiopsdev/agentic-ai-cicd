from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', 'localhost']  # Define a whitelist of allowed hosts
    if host in allowed_hosts:
        subprocess.call(['ping', host], shell=False)
    else:
        raise ValueError('Host is not allowed')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}