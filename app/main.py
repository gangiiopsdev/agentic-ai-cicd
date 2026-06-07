from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    args = ['ping', host]
    subprocess.call(args)

def safe_ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Unsafe host')
    args = ['ping', host]
    subprocess.call(args)

def is_safe_host(host: str) -> bool:
    # Add your logic to validate the host here
    return True

@app.get("/ping")
def ping_host(host: str):
    return safe_ping(host)