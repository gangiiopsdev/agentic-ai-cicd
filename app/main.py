from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation with validation and escaping
    if host.strip().isalnum():
        subprocess.run(['ping', host], check=True)
    else:
        raise ValueError('Invalid hostname')

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)