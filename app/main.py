from fastapi import FastAPI
import subprocess
from typing import List

app = FastAPI()

def validate_host(host: str) -> bool:
    # Add your validation logic here
    return host.strip() and all(c.isalnum() or c in ['.', '-', '_'] for c in host)

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "invalid host"}
    subprocess.call(['ping', host])
    return {"status": "completed"}