from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    valid_hosts = ['example.com', 'google.com']  # Define a whitelist of allowed hosts
    if host in valid_hosts:
        args = ['ping', host]
        subprocess.call(args)
    else:
        raise ValueError('Host not allowed')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}