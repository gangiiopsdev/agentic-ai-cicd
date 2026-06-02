from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation with validation
    if host.strip().isalnum():
        subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid hostname')

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)