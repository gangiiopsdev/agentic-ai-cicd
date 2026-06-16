from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and validating input
    if not is_valid_host(host):
        return {'status': 'invalid host'}
    subprocess.call(['ping', '-c', '1', host])
    return {'status': 'completed'}

def is_valid_host(host: str) -> bool:
    # Basic validation to allow only alphanumeric characters and hyphens
    import re
    return re.match(r'^[a-zA-Z0-9-]+$', host) is not None