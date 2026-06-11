from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_' for c in host):
        return subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid hostname')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}