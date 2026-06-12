from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using list arguments for subprocess.call
    subprocess.run(['ping', host], check=True, shell=False)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {"error": "Invalid host"}
    safe_ping(host)
    return {"status": "completed"}

def is_safe_host(host: str):
    # Implement your logic to check if the host is safe
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts