from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Implement a safe host check logic here (e.g., whitelist)
    allowed_hosts = ['example.com', 'another-example.com']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Invalid host")
    # Secure implementation using subprocess.Popen with shell=False and appropriate argument handling
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}