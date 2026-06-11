from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    subprocess.call(['ping', '-c', '1', host])

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)