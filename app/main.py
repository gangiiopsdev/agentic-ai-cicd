from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Define a list of allowed hosts or implement other validation logic here
    allowed_hosts = ['127.0.0.1', '::1']
    if host in allowed_hosts:
        subprocess.call(['ping', host])
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)