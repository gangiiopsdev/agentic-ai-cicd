from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_host(host):
    safe_hosts = ['google.com', 'example.com']  # Define a list of allowed hosts
    return host in safe_hosts

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {"status": "error", "message": "Host is not allowed"}
    sanitized_host = shlex.quote(host)
    subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {"status": "completed"}