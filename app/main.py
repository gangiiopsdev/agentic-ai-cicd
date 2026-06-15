from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    if not host or len(host) > 255:
        raise ValueError("Invalid host")
    return shlex.quote(host)

@app.get="/ping")
def ping(host: str):
    safe_host = validate_host(host)
    subprocess.call(["ping", safe_host])
    return {"status": "completed"}