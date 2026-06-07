from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for c in host):
        raise ValueError('Invalid characters in hostname')
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):\n    safe_ping(host)\n    return {"status": "completed"}