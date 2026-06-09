from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate and sanitize input if necessary
    if all(c.isalnum() for c in host) and len(host.split('.')) == 4:
        subprocess.run(['ping', host], capture_output=True, text=True)
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)