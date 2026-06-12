from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Ensure the host input is sanitized before passing to subprocess.run
    if not host.isalnum() and '@' not in host:
        raise ValueError('Invalid host name')
    subprocess.run(['ping', host], check=True)

@app.get('/ping')
def ping_wrapper(host: str):
    return ping(host)