from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Using a whitelist of allowed hosts or validating host input is safer.
    allowed_hosts = ['127.0.0.1', '::1']
    if host in allowed_hosts:
        subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}