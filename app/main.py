from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Using subprocess.run instead of subprocess.call
    subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    if 'localhost' in host or '127.0.0.1' in host:
        safe_ping(host)
    else:
        raise ValueError('Invalid host')

    return {"status": "completed"}