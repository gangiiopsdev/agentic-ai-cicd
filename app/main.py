from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation with input validation and escaping
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    sanitized_host = subprocess.list2cmdline([host])
    subprocess.run(['ping', sanitized_host], check=True)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)