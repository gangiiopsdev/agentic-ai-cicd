from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate input before passing it to subprocess
    if not host.isalnum() or '..' in host:
        raise ValueError('Invalid host name')
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return {'result': ping(host)}