from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host):
    # Define allowed characters and lengths for hostnames/IP addresses
    return all(c.isalnum() or c in ['.', '-'] for c in host) and len(host) > 0 and len(host) <= 255

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "invalid host"}
    command = ["ping", shlex.quote(host)]
    subprocess.call(command)
    return {"status": "completed"}