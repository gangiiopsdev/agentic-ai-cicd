from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        raise ValueError('Invalid host name')
    args = ['ping', host]
    subprocess.call(args)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)