from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate host parameter
    if not host.isalnum():
        raise ValueError('Invalid host name')
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)