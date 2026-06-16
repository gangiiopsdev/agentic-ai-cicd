from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation using Popen with args instead of shell=True
    if isinstance(host, str) and len(host.strip()) > 0:
        subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        raise ValueError('Invalid host input')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}