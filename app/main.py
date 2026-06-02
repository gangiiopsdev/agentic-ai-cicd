from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host):
    # Basic validation: ensure host contains only alphanumeric characters and hyphens.
    return host.replace('-', '').isalnum()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host name')

    # Secure implementation using shlex.split to safely handle command arguments
    args = ['ping'] + shlex.split(host)
    subprocess.call(args)

    return {"status": "completed"}