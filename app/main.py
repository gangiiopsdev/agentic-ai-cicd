from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if not validate_host(host):
        raise ValueError('Invalid host')
    args = ['ping', host]
    subprocess.run(args, check=True)

def validate_host(host: str) -> bool:
    # Implement your validation logic here
    return all(c.isalnum() or c in '-.' for c in host)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)