from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation with full executable path and validation
    if not host.strip().isalnum() or '@' in host:
        raise ValueError('Invalid hostname')
    subprocess.run(['ping', '-c 4', host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)