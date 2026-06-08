from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if host.strip() == 'localhost' or host.strip() == '127.0.0.1':
        subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):

    # Safe implementation
    safe_ping(host)

    return {"status": "completed"}