from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def validate_host(host):
    if not host or len(host) > 255:
        raise ValueError("Invalid host name")
    # Enhanced validation to prevent injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host name")
    return host

@app.get("/ping")
def ping(host: str):
    validated_host = validate_host(host)
    subprocess.run(["ping", "/dev/tcp/{validated_host}/80"], check=True)
    return {"status": "completed"}