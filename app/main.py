from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Define a list of allowed hosts or IP ranges
    allowed_hosts = ['192.168.1.1', '10.0.0.1']
    if host not in allowed_hosts:
        return False
    return True

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not safe_ping(host) or not host.isalnum() or len(host) > 64:
        return {"status": "error", "message": "Invalid input"}
    subprocess.call(["ping", host])
    return {"status": "completed"}