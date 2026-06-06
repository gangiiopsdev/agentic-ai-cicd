from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_ping(host: str):
    if not all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_:' for c in host):
        raise ValueError('Invalid characters in host name')
    subprocess.call(['ping', quote(host)])

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}