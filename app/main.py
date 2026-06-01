from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation with input validation and whitelisting
    allowed_hosts = ['google.com', 'bing.com']
    if host not in allowed_hosts:
        raise ValueError("Invalid hostname")
    args = ['ping', host]
    subprocess.call(args)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)