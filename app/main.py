from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for c in host):
        subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}