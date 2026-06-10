from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    sanitized_host = host.strip()
    if not sanitized_host.isalnum():
        raise ValueError('Invalid host name')
    subprocess.run(['ping', sanitized_host], check=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)