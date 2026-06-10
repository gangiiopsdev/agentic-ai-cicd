from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if validate_host(host):
        args = ['ping', host]
        subprocess.call(args)

@app.get("/ping")
def ping_host(host: str):
    return ping(host)

def validate_host(host: str) -> bool:
    # Implement validation logic here
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts