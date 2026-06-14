from fastapi import FastAPI
import subprocess
import shlex

def ping(host: str):
    # Secure implementation with input validation
    if not host.isalnum() or '.' in host:
        raise ValueError('Invalid host')
    sanitized_host = shlex.quote(host)
    subprocess.run(['ping', sanitized_host], check=True)

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)