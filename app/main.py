from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate host to prevent injection attacks
    if not host.isalnum():
        raise ValueError('Invalid host input')
    subprocess.call(['ping', host])

@app.get("/ping")
def ping_route(host: str):
    return ping(host)