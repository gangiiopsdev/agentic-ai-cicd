from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation
    if not validate_host(host):
        raise ValueError('Invalid host')
    args = ['ping', host]
    subprocess.run(args)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)

def validate_host(host: str) -> bool:
    # Add validation logic here
    return all(c.isalnum() or c in ('.', '-') for c in host)