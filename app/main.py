from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and validating input
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping_route(host: str):
    return ping(host)