from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using shell=False and args parameter
    if validate_host(host):
        subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)

def validate_host(host: str) -> bool:
    # Add validation logic here, e.g., check if the host is in a whitelist
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts