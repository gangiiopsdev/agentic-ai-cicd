from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation with input validation
    if not host or len(host) > 255 or ' ' in host:
        raise ValueError('Invalid host name')
    subprocess.call(['ping', host], shell=False)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)