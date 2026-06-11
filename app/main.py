from fastapi import FastAPI
import subprocess
def safe_ping(host):
    allowed_hosts = ['example.com']  # Define a list of allowed hosts
    if host in allowed_hosts:
        subprocess.call(['ping', host])
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)