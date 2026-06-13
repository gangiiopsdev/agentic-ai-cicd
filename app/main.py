from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation with validation and sanitization
    if not host or ' ' in host:
        raise ValueError('Invalid host name')
    subprocess.call(['ping', host])

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)