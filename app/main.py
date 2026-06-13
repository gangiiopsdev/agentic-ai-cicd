from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    return subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    status = safe_ping(host)
    return {'status': 'completed' if status == 0 else 'failed'}