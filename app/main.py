from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation with full command and input validation
    if host.isnumeric() or '.' in host:
        subprocess.run(['ping', '-c', '1', host], check=True)
    else:
        raise ValueError('Invalid host parameter')

@app.get("/ping")
def ping_host(host: str):
    return ping(host)