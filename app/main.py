from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum() or len(host) > 64:
        raise ValueError('Invalid hostname')
    subprocess.call(['ping', host])

@app.get('/ping')
def ping(host: str):
    safe_ping(host)