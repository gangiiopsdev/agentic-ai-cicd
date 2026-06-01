from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Basic validation: ensure host contains only alphanumeric characters and hyphens.
    return host.replace('-', '').isalnum()

@app.get("/ping")
def ping(host: str):

    if not is_valid_host(host):
        raise ValueError('Invalid host name')

    # Safe implementation
    subprocess.call(['ping', host])

    return {"status": "completed"}