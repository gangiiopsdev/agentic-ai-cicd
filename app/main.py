from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate and sanitize the host input
    if not all(c.isalnum() for c in host) or len(host) > 64:
        raise ValueError("Invalid host")
    args = ['ping', host]
    subprocess.call(args)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)