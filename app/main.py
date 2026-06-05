from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation with validation and sanitization
    if host.isalnum():
        subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid input')

@app.get("/ping")
def ping_route(host: str):
    return ping(host)