from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation with input validation and escaping
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    sanitized_host = subprocess.list2cmdline([host])
    subprocess.call(['ping', sanitized_host])

@app.get("/ping")
def ping_route(host: str):
    return ping(host)