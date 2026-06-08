from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate and sanitize host input
    if not host or len(host) > 255:
        raise ValueError('Invalid host name')
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)