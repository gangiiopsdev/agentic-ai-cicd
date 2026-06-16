from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using a whitelist of allowed hosts or by validating input
    allowed_hosts = ['example.com', 'localhost']
    if host in allowed_hosts:
        subprocess.call(['ping', host])
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)