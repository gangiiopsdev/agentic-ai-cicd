from fastapi import FastAPI
import subprocess
def ping(host: str):
    if not host.isalnum() or ' ' in host:
        raise ValueError('Invalid host name')
    safe_host = [host]  # Ensure host is treated as a list of arguments to avoid shell=True and command injection
    subprocess.run(['ping', '-c', '1'] + safe_host, capture_output=True, text=True, check=True)
app = FastAPI()
@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)