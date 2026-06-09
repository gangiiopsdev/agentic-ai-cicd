from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation
    if all(c.isalnum() or c in ('.', '-') for c in host):
        subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid host name')

@app.get("/ping")
def ping_route(host: str):
    return ping(host)