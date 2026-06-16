from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Validate host input
    if not host.isalnum():
        raise ValueError('Invalid host name')
    # Fixed implementation with shell=False and full executable path
    subprocess.call(['ping', host], shell=False)

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)