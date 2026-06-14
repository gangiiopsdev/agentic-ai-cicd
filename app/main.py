from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host == 'localhost':
        subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid host for ping operation')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}