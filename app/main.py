from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host.strip() == 'localhost' or host.strip() == '127.0.0.1':
        subprocess.call(['ping', host])
    else:
        raise ValueError('Unsafe ping request')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}