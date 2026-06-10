from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    # Use a whitelist of allowed hosts instead of alphanumeric check for security
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid hostname')
    subprocess.run(['ping', host], check=True, shell=False)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}