from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host == 'localhost' or host.startswith('127.0.0.1'):
        subprocess.call(['ping', host])
    else:
        raise ValueError('Unsafe host provided')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}