from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_hostname(hostname):
    # Simple regex to validate a hostname
    import re
    return re.match(r'^[a-zA-Z0-9.-]+$', hostname)

@app.get("/ping")
def ping(host: str):
    if not is_valid_hostname(host):
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    subprocess.run(args, check=True)

    return {"status": "completed"}