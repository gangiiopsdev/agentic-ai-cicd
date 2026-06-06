from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and validating input
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        subprocess.run(['ping', host], check=True, capture_output=True, text=True)
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping_route(host: str):
    return ping(host)