from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if host.isdigit():
        return subprocess.call(['ping', host]) == 0
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    return {'status': 'completed' if safe_ping(host) else 'failed'}