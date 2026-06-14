from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not all(c.isalnum() or c in ['-', '.', '_'] for c in host):
        raise ValueError('Invalid hostname')
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)