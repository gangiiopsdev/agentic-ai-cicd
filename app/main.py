from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Ensure host input is properly validated and sanitized
    if not host.isalnum():
        raise ValueError('Invalid host name')
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)