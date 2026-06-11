from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation with input validation and sanitization
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    subprocess.call(['ping', host])

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)