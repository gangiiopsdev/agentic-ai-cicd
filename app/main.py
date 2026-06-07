from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation with input sanitization and validation
    if host.isalnum():
        subprocess.run(['ping', host], check=True)
    else:
        raise ValueError('Invalid host input')

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)