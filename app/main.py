from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Implement your logic to check if the host is safe
    allowed_hosts = ['127.0.0.1', '::1']  # Example list of allowed hosts
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        # Use subprocess.run for better security and more control over the process
        subprocess.run(["ping", host], check=True, shell=False)
        return {"status": "completed"}
    else:
        return {"status": "failed", "message": "Unsafe host"}