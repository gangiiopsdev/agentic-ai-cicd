from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using list for command arguments
    subprocess.call(['ping', host], shell=False)

def validate_host(host: str) -> bool:
    # Add validation logic here (e.g., allow only certain hosts, use a whitelist)
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        safe_ping(host)
        return {"status": "completed"}
    else:
        return {"status": "Invalid host", "error": "Host not allowed"}