from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host.strip() == 'localhost' or host.strip() == '127.0.0.1':
        return subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    return {'status': safe_ping(host)}