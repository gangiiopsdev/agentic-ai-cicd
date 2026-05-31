from fastapi import FastAPI
import subprocess
def is_safe_host(host):
    # Define a list of safe hosts or patterns
    allowed_hosts = ['127.0.0.1', 'localhost']
    return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Unsafe host")
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}