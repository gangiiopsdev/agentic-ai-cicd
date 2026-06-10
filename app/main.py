from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation
    if is_valid_host(host):
        subprocess.call(['ping', host], shell=False)
    else:
        raise ValueError('Invalid host name')

@app.get("/ping")
def ping_endpoint(host: str):
    return {'status': ping(host)}

def is_valid_host(host: str) -> bool:
    import re
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return bool(pattern.match(host))