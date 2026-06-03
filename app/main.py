from fastapi import FastAPI
import subprocess
def is_safe_host(host):
    safe_hosts = ['127.0.0.1', 'localhost']
    return host in safe_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Invalid host")
    # Secure implementation using subprocess.run instead of subprocess.call
    result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed", "output": result.stdout.decode()}